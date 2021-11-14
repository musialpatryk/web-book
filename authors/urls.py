from django.conf.urls import url
from django.urls import include
from . import views

app_name = 'authors'

urlpatterns = [
    url(r'^$', views.authors_list, name="list"),
    # url(r'^create/$', views.book_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.author_details, name="details"),
]