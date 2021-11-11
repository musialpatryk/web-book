from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls')),
    url(r'^authors/', include('authors.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.home),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^socials/', include('allauth.urls')),
]

urlpatterns += staticfiles_urlpatterns()
handler404 = "webBookApi.views.error_404"
handler500 = "webBookApi.views.error_500"
