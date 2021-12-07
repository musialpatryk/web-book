from django.conf.urls import url
from .import views

app_name = 'role_requests'

urlpatterns = [
    url(r'^$', views.role_request_create, name="list"),
    url(r'^create/$', views.role_request_create, name="create"),
    # url(r'^accept/$', views.accept_review, name="accept"),
    # url(r'^reject/$', views.reject_review, name="reject"),
]