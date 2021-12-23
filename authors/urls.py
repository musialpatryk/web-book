from django.conf.urls import url
from django.urls import include
from . import views

app_name = 'authors'

urlpatterns = [
    url(r'^$', views.authors_list, name="list"),
    url(r'^create/$', views.authors_create, name="create"),
    url(r'^requests/$', views.author_requests, name="requests"),
    url(r'^remove/(?P<pk>\d+)/$', views.author_delete, name="remove_author"),
    url(r'^requests/accept$', views.author_accept, name="accept"),
    url(r'^requests/reject$', views.author_reject, name="reject"),
    url(r'^(?P<slug>[\w-]+)/$', views.author_details, name="details"),
]