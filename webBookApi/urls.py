from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^role_requests/', include('role_requests.urls')),
    url(r'^authors/', include('authors.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.home),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^socials/', include('allauth.urls')),
    #won't redirect in accountsapp
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
handler404 = "webBookApi.views.error_404"
handler500 = "webBookApi.views.error_500"
