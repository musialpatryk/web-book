from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from accounts.decorators import admin_only
from .models import Author
from django.core.paginator import Paginator
from helpers.pagination_tool import PaginationTool


@login_required(login_url='accounts:login')
def authors_list(request):
    p = Paginator(Author.objects.all().order_by('name'), 2)
    page = request.GET.get('page')
    authors = p.get_page(page)
    return render(request, 'authors/authors_list.html', {'authors': authors})


@login_required(login_url='accounts:login')
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

        return HttpResponseRedirect("/authors/")

