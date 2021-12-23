from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accounts.models import get_users
from authors.forms.request_form import AuthorRequestForm
from books.models import Genre
from general import mailing
from .forms.requests_list_form import RequestListForm
from .models import Author
from django.core.paginator import Paginator
from accounts.decorators import allowed_users, admin_only
from django.contrib import messages


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def authors_list(request):
    p = Paginator(Author.objects.all().filter(status='A').order_by('name'), 10)
    page = request.GET.get('page')
    authors = p.get_page(page)
    return render(request, 'authors/authors_list.html', {'authors': authors})


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def author_details(request, slug):
    author = Author.objects.get(slug=slug)
    # if null === book:
    return render(request, 'authors/authors_details.html', {'author': author})


@login_required(login_url='accounts:login')
@admin_only
def author_delete(request, pk):
    if request.method == 'POST':
        author = Author.objects.get(pk=pk)
        author.delete()
        messages.success(request, "Pomyslnie usunieto autora")

        return HttpResponseRedirect("/authors/")


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def authors_create(request):
    if request.method == 'POST':
        authors_data = request.POST

        genre = Genre.objects.get(pk=int(authors_data['genre']))
        new_author = Author.objects.create_author(
            authors_data['name'],
            genre,
            authors_data['description'],
            authors_data['birthDate'],
            authors_data['slug'],
            request.FILES['image']
        )

        new_author.save()

        recipients = get_users('admin')
        mailing.send_mails('New Author Added', 'Hi, New item added to your request list \nhttp://127.0.0.1:8000/authors/requests/', recipients)

        return HttpResponseRedirect('/')


    genre_options = []
    for genre in Genre.objects.all():
        genre_options.append((genre.id, genre.__str__()))

    form = AuthorRequestForm(genre=genre_options)
    return render(request, 'authors/authors_create.html', {'form': form})


@login_required(login_url='accounts:login')
@admin_only
def author_requests(request):
    forms = []
    for author in Author.objects.filter(status='P'):
        forms.append(RequestListForm(author=author))
    p = Paginator(forms, 10)
    page = request.GET.get('page')
    forms = p.get_page(page)

    return render(request, 'authors/author_requests.html', {'forms': forms})


@login_required(login_url='accounts:login')
@admin_only
def author_accept(request):
    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = Author.objects.get(pk=author_id)
        author.status = 'A'
        author.save()
        author_status_change_message(request)

    recipients = get_users('viewer')
    mailing.send_mails('New Author has been added', 'Hi, Author: ' + author.name + ' was approved. Go to BookWeb and check it now \nhttp://127.0.0.1:8000/books/', recipients)

    return HttpResponseRedirect(reverse('authors:requests'))


@login_required(login_url='accounts:login')
@admin_only
def author_reject(request):
    if request.method == 'POST':
        author_id = request.POST['author_id']
        author = Author.objects.get(pk=author_id)
        author.status = 'R'
        author.save()
        author_status_change_message(request)

    return HttpResponseRedirect(reverse('authors:requests'))


def author_status_change_message(request):
    messages.success(request, 'Pomyslnie zmieniono status autora')
