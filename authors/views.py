from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Author
from helpers.pagination_tool import PaginationTool
from django.http import HttpResponse

@login_required(login_url='accounts:login')
def authors_list(request):
    return render(request, 'authors/authors_list.html', {'authors': PaginationTool(Author(), request.GET.get('page'), request.GET.get('limit')).get_data()})

@login_required(login_url='accounts:login')
def author_details(request, slug):
    author = Author.objects.get(slug=slug)
    return render(request, 'authors/authors_details.html', {'author': Author.objects.get(id=id)})

