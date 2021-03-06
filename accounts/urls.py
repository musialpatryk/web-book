from django.conf.urls import url
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^profile/$', views.user_profile_view, name="profile"),
    url(r'^profile/update/$', views.UpdateUser_profile_view, name="profileUpdate"),
]
