from pickle import TRUE
from django.db import models
import uuid
from  datetime import datetime



class Course (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    title = models.CharField(max_length=200)
    # img = models.URLField(null=True,blank=True)
    # upload_img = models.ImageField(null=True,blank = True)
    discription = models.TextField(null=True,blank = True)
    price = models.BigIntegerField()
    url = models.URLField(unique=True)
    students = models.BigIntegerField(default=0)
    time = models.BigIntegerField(help_text="timestamp in min")
    time_str = models.CharField(max_length=500)
    lang = models.CharField(max_length=50)
    score = models.BigIntegerField(default=0)
    addTime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.title)

class SocalMedia(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    platform = models.CharField(max_length=200)

    def __str__(self):
        return self.platform



class User (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=25,blank=True,null=True)
    ip = models.CharField(max_length=200)
    score = models.IntegerField(default=0)
    isVerified = models.BooleanField(default=False)
    bio = models.CharField(max_length=300,default="Searcher")
    date = models.DateTimeField(default=datetime.now())
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.name + " | " + str(self.id)

class UserSocalMedia(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    media = models.ForeignKey(SocalMedia,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    url = models.URLField()


class Publisher (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    url = models.URLField()
    name= models.CharField(max_length=200,null=True,blank=True)
    img = models.ImageField()
    SEORank = models.BigIntegerField(default=0)
    LastIndexed = models.DateTimeField()
    CreatedDate = models.DateTimeField()
    isScrapAlgorithmWrite = models.BooleanField("Is Published",default=False)
    indexCoder = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class PublisherSocalMedia (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    media = models.ForeignKey(SocalMedia,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    url = models.URLField()


class Publish (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,unique=True)
    is_visible = models.BooleanField()


    def __str__(self):
        return str(self.publisher)

class TAG (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
    name =models.CharField(max_length=200)
    image = models.ImageField(blank=True,null=True)
    rank = models.IntegerField(default=0)


    def __str__(self):
        return str(self.name)

class Teacher (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=200,unique=True)
    score = models.BigIntegerField(default=0)

    def __str__(self):
        return str(self.name)


class TeacherSocalMedia(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    media = models.ForeignKey(SocalMedia,on_delete=models.CASCADE)
    url = models.URLField()


class CourseTAG (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,unique=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    tag = models.ManyToManyField(TAG,related_name='course_tag_rel')
    rank = models.JSONField()

    def __str__(self):
        return str(self.course)


class TeacherMakeCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,unique=True)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.teacher)


class CourseComment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    state = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    comment = models.TextField()
    replay = models.ForeignKey("CourseComment",on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return str(self.id)

class UserAddComment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(CourseComment,on_delete=models.CASCADE)

class UserStarComment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(CourseComment,on_delete=models.CASCADE)

class UserLikeComment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(CourseComment,on_delete=models.CASCADE)


class UserSearchCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    search = models.CharField(max_length=500,blank=True,null=True)
    count = models.BigIntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.search)


class ReportPublisher (models.Model):
    id = models.UUIDField(primary_key = True,default=uuid.uuid4,editable=False)
    publisher = models.ForeignKey( Publisher ,on_delete=models.CASCADE)
    msg = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.publisher)

class ReportCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    msg =models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course)

class Credit (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    monney = models.BigIntegerField(default=5000) # Default is 5000 toman
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.monney)

class Payment (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=200)
    price = models.BigIntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.title)

class Pay (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.publisher)


class ClickCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.course)

class WatchCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.course)


class SearchLog(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    search = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.date) + " | " + str(self.search)


class contactUs (models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return str(self.email)


class Article(models.Model):
    title = models.CharField(max_length=200)


    def get_absolute_url(self):
        return "/%i/" % self.id
