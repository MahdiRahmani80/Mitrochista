from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.static import serve
from main.sitemap import TAGSitemap,MasterSM,CourseSM,PublisherSM


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("main.urls")),

    # SiteMap
    path('tag.xml', sitemap, {'sitemaps': {'tag' : TAGSitemap}},name='django.contrib.sitemaps.views.sitemap'),
    path('master.xml', sitemap, {'sitemaps': {'master':MasterSM},},name='django.contrib.sitemaps.views.sitemap'),
    path('course.xml', sitemap, {'sitemaps': {'course':CourseSM},},name='django.contrib.sitemaps.views.sitemap'),
    path('publisher.xml', sitemap, {'sitemaps': {'publisher':PublisherSM},},name='django.contrib.sitemaps.views.sitemap'),

    path('api-auth/', include('rest_framework.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
