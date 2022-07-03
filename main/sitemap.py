from django.contrib.sitemaps import Sitemap
from .models import TAG,Publish,Publisher,Teacher
from datetime import datetime

class TAGSitemap (Sitemap):
    def items(self):
        return TAG.objects.all()

    def lastmod(self, obj):
	    return datetime.now()

    def location(self,obj):
        return '/tag/%s' % (str(obj.name) , )


class MasterSM(Sitemap):
    def items(self):
        return Teacher.objects.all()

    def lastmod(self, obj):
	    return datetime.now()

    def location(self,obj):
        return '/teacher/%s/' % (str(obj.name) , )


class PublisherSM(Sitemap):
    def items(self):
        return Publisher.objects.all()

    def lastmod(self, obj):
	    return datetime.now()

    def location(self,obj):
        return '/publisher/%s/' % (str(obj.id) , )


class CourseSM(Sitemap):
    def items(self):
        return Publish.objects.all()

    def lastmod(self, obj):
	    return datetime.now()

    def location(self,obj):
        return '/course/%s/%s/' % (str(obj.course.title).replace(" ","%20") , str(obj.course.id) )

