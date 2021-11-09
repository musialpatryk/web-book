from django.shortcuts import render
from .models import Author
from helpers.pagination_tool import PaginationTool


def authors_list(request):

    paginator = PaginationTool(request, Author())
    return render(request, 'authors_list.html', {'authors': paginator.get_data()})


def author_details(request, id):
    return render(request, 'author_details.html', {'author': Author.objects.get(id=id)})

