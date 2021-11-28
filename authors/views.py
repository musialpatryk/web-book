from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Author
from django.core.paginator import Paginator
from helpers.pagination_tool import PaginationTool
from accounts.decorators import allowed_users, unauthenticated_user, admin_only


@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['viewer', 'admin'])
def authors_list(request):
    # offset, limit = PaginationTool(request.GET.get('page'), request.GET.get('limit')).get_data()
    # return render(request, 'authors/authors_list.html', {'authors': Author.objects.all()[offset:limit]})
    p = Paginator(Author.objects.all(), 2)
    page = request.GET.get('page')
    authors = p.get_page(page)
    return render(request, 'authors/authors_list.html', {'authors': authors})


@allowed_users(allowed_roles=['viewer', 'admin'])
@login_required(login_url='accounts:login')
def author_details(request, slug):
    author = Author.objects.get(slug=slug)
    # if null === book:
    return render(request, 'authors/authors_details.html', {'author': author})

