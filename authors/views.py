from django.shortcuts import render
from .models import Author
from django.http import HttpResponse
from helpers import pagination_helper
from django.core.paginator import Paginator
from helpers.pagination_helper import PaginationTool


def authors_list(request):

    paginator = PaginationTool(request, Author())
    return render(request, 'authors_list.html', {'authors': paginator.get_data()})


def author_details(request, id):
    return render(request, 'author_details.html', {'author': Author.objects.get(id=id)})

