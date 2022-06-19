from django.urls import path, include,re_path
from . import views


urlpatterns = [
    path('',views.index),
    re_path(r'^tag/(?P<tag>.*)/$',views.tag),
    re_path(r'^course/(?P<course>.*)/$',views.course),
    re_path(r'^teacher/(?P<teacher>.*)/$',views.teacher),
    path('api/', include("main.api.urls")),

]
