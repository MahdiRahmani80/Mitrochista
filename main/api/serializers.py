from main import models
from rest_framework import serializers



class Tag (serializers.ModelSerializer):

    class Meta:
        model = models.TAG
        fields = '__all__'

class CourseSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'

class CourseSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'


class CourseSerializer (serializers.ModelSerializer):

    class Meta:
        model = models.Course
        fields = '__all__'

class Teacher (serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class CourseTag (serializers.ModelSerializer):
    class Meta:
        model = models.CourseTAG
        fields = '__all__'


class TeachersCourse (serializers.ModelSerializer):
    class Meta:
        model = models.TeacherMakeCourse
        fields = '__all__'

class PublishCourse (serializers.ModelSerializer):
    class Meta:
        model = models.Publish
        fields = '__all__'


class Publisher (serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = '__all__'
