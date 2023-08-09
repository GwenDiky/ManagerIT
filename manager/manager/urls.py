from django.contrib import admin
from django.urls import path, include
from main.views import index
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import TaskSitemap

sitemaps = {
    'tasks': TaskSitemap,
}

#маршрутизатор
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]
