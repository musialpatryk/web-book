from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', include('books.urls')),
    url(r'^reviews/', include('reviews.urls')),
    url(r'^authors/', include('authors.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.home),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^socials/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
handler404 = "webBookApi.views.error_404"
handler500 = "webBookApi.views.error_500"
