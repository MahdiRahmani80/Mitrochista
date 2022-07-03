from django.urls import path, include,re_path
from . import views


urlpatterns = [
    path('',views.index),
    path('explore/',views.result),
    path('pannel/signin/',views.publisher_signin),
    path('contact/',views.contact),
    path('partnership/',views.requestPartnership),
    re_path(r'^pannel/website/(?P<id>.*)$',views.websitePannel),
    re_path(r'^tag/(?P<tag>.*)/$',views.tag),
    re_path(r'^course/(?P<course>.*)/(?P<id>.*)/$',views.course),
    path('course/',views.result),
    re_path(r'^publisher/(?P<pub_id>.*)/$',views.coursePublisher),
    path('publisher/',views.publisher),
    re_path(r'^teacher/(?P<teacher>.*)/$',views.teachersCourse),
    re_path(r'^teacher/$',views.teacher),
    path('api/', include("main.api.urls")),

]


