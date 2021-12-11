from django.conf.urls import url
from . import views

app_name = 'reviews'
urlpatterns = [
    url(r'^$', views.review_list, name="list"),
    url(r'^create/$', views.review_create, name="create"),
    url(r'^accept/$', views.accept_review, name="accept"),
    url(r'^reject/$', views.reject_review, name="reject"),
    # url(r'^requests/accept$', views.book_accept, name="accept"),
    # url(r'^requests/reject$', views.book_reject, name="reject"),
    # url(r'^requests/$', views.book_requests, name="requests"),
    # url(r'^(?P<slug>[\w-]+)/$', views.book_details, name="details"),
    # url('search/<string:title>/', views.search_book, name='search'),
]