from django.conf.urls import url
from . import views

app_name = 'reviews'
urlpatterns = [
    url(r'^$', views.review_list, name="list"),
    url(r'^create/$', views.review_create, name="create"),
    url(r'^accept/$', views.accept_review, name="accept"),
    url(r'^reject/$', views.reject_review, name="reject"),
]