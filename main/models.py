from distutils.command import upload
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
    url = models.URLField(unique=True,max_length=5000)
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
    phone = models.CharField(max_length=20,unique=True)
    email = models.EmailField(blank=True,null=True)
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
    password = models.CharField(max_length=500)
    connectionWay =  models.CharField(max_length=600,help_text="email or phone",unique=True)
    img = models.ImageField(upload_to="Publisher/Image")
    SEORank = models.BigIntegerField(default=0)
    LastIndexed = models.DateTimeField(auto_now_add=True)
    CreatedDate = models.DateTimeField(auto_now_add=True)
    isScrapAlgorithmWrite = models.BooleanField("Is Published",default=False)
    isUP = models.BooleanField(default=False)
    indexCoder = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):

        if self.isUP:
            if not Credit.objects.filter(publisher=self):
                Credit.objects.create(publisher=self)

        if self.isScrapAlgorithmWrite:
            Publish.objects.filter(publisher__id=self.id).update(is_visible=True)

        super(Publisher,self).save(*args,**kwargs)



class PublisherSocalMedia (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    media = models.ForeignKey(SocalMedia,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    url = models.URLField()


class Publish (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
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
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publish,on_delete=models.CASCADE)
    tag = models.ManyToManyField(TAG,related_name='course_tag_rel')
    rank = models.JSONField()
    master = models.CharField(max_length=300)

    def __str__(self):
        return str(self.course)


class TeacherMakeCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
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

class Payment(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    idpay_id = models.CharField(max_length=500)
    amount = models.CharField(max_length=5000)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    stp1DataReseveIDPAY = models.TextField(null=True,blank=True)
    stp2DataReseveIDPAY = models.TextField(null=True,blank=True)
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.publisher)


class ClickCourse (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    ip = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

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
    subject = models.CharField(max_length=300, blank=True, null=True)
    text = models.TextField()
    time = models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.email)


class newsLetter(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    email = models.EmailField()

    def __str__(self) :
        return str(self.email)


    # def get_absolute_url(self):
        # return "/%i/" % self.id
