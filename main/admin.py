from django.contrib import admin
from . import models



class User(admin.ModelAdmin):
    search_fields = ['name','email','phone','ip','bio']
    list_display = ['name','id','isVerified']
    list_filter = ('date','isVerified')

class CourseComment(admin.ModelAdmin):
    search_fields = ['comment','id']
    list_display = ['id','course','date']
    list_filter = ('date','state')

class Course(admin.ModelAdmin):
    list_display = ['title','id','price','time','score',]
    search_fields = ['title','students','discription']
    list_filter = ('lang',)

class Tag (admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name','id','rank']
    list_filter = ('rank',)

class CourseTag (admin.ModelAdmin):
    list_display = ['course','publisher']
    list_filter = ('publisher',)

class Publisher (admin.ModelAdmin):
    search_fields = ['name','url']
    list_display = ['url','name','id','isScrapAlgorithmWrite']
    list_filter = ('isScrapAlgorithmWrite','LastIndexed','CreatedDate')

class Teacher (admin.ModelAdmin):
    search_fields = ['name',]
    list_display = ['name','score']
    list_filter = ('score',)

class TeacherMkCurse (admin.ModelAdmin):
    search_fields = ['Course','teacher']
    list_display = ['teacher','Course','date']
    list_filter = ('teacher',)

class PublisherMedia (admin.ModelAdmin):
    list_display = ['publisher','media']
    list_filter = ('media','publisher')

class PublishCourse (admin.ModelAdmin):
    list_display = ['course','publisher','is_visible']
    list_filter = ('publisher',)

class TeacherSocalMediaAdmin(admin.ModelAdmin):
    list_display = ['teacher','media','url']
    list_filter = ('media',)

admin.site.register(models.Course,Course)
admin.site.register(models.SocalMedia)
admin.site.register(models.User,User)
admin.site.register(models.UserSocalMedia)
admin.site.register(models.Publisher,Publisher)
admin.site.register(models.PublisherSocalMedia,PublisherMedia)
admin.site.register(models.Publish,PublishCourse)
admin.site.register(models.TAG,Tag)
admin.site.register(models.Teacher,Teacher)
admin.site.register(models.TeacherSocalMedia,TeacherSocalMediaAdmin)
admin.site.register(models.CourseTAG,CourseTag)
admin.site.register(models.TeacherMakeCourse,TeacherMkCurse)
admin.site.register(models.CourseComment,CourseComment)
admin.site.register(models.UserAddComment)
admin.site.register(models.UserStarComment)
admin.site.register(models.UserLikeComment)
admin.site.register(models.UserSearchCourse)
admin.site.register(models.ReportPublisher)
admin.site.register(models.ReportCourse)
admin.site.register(models.Credit)
admin.site.register(models.Payment)
admin.site.register(models.Pay)
admin.site.register(models.ClickCourse)
admin.site.register(models.WatchCourse)
admin.site.register(models.SearchLog)
admin.site.register(models.contactUs)
admin.site.register(models.Article)

