from django.urls import path
from . import views


urlpatterns = [
    path('create/tag/',views.CreateTAG.as_view()),
    path('create/course/',views.AddCourse.as_view()),
    path('get/course/',views.GetCourse.as_view()),
    path('update/course/<uuid:id>',views.UpdateCourse.as_view()),
    path('create/teacher/',views.AddTeacher.as_view()),
    path('update/teacher/<str:name>',views.UpdateCourseTeacher.as_view()),
    path('create/course/teacher/',views.AddCourseTeacher.as_view()),
    path('create/coursetag/',views.AddCourseTag.as_view()),
    path('create/course/publish/',views.PublishCourse.as_view()),

]



