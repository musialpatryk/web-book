from django.conf.urls import url
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.book_list, name="list"),
    url(r'^create/$', views.book_create, name="create"),
    url(r'^requests/accept$', views.book_accept, name="accept"),
    url(r'^requests/reject$', views.book_reject, name="reject"),
    url(r'^remove/(?P<pk>\d+)/$', views.book_delete, name="remove_book"),
    url(r'^requests/$', views.book_requests, name="requests"),
    url(r'^(?P<slug>[\w-]+)/$', views.book_details, name="details"),
    url('search/<string:title>/', views.search_book, name='search'),
]

