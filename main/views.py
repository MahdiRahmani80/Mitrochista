from django.shortcuts import render
from . import models
from .search import search

# INDEX
def index(request):

    search_text = request.POST.get('search')
    if search_text:
        search (search_text,models.CourseTAG,models.TAG)



    return render(request,'index.html')


# TAG
def tag (request,tag=None):

    TAG = models.TAG.objects.get(name=tag.replace("%20", " "))

    d= {
        'tag':TAG,
    }
    return render(request,'tag.html',d)



# COURSE
def course (request,course=None):

    COURSE = models.Course.objects.get(title=course.replace("%20", " "))

    d= {
        'tag':COURSE,
    }
    return render(request,'tag.html',d)



# TEACHER
def teacher (request,teacher=None):

    TEACHER = models.Teacher.objects.get(name=teacher.replace("%20", " "))

    d= {
        'tag':TEACHER,
    }
    return render(request,'tag.html',d)



