from django.shortcuts import render
from .models import Author
from helpers.pagination_tool import PaginationTool


def authors_list(request):
    return render(request, 'authors_list.html', {'authors': PaginationTool(Author(), request.GET.get('page'), request.GET.get('limit')).get_data()})


def author_details(request, id):
    return render(request, 'author_details.html', {'author': Author.objects.get(id=id)})

