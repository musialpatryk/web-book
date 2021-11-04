from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.home),
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
