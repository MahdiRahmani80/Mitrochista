from main import models
from . import serializers
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from main import models
from rest_framework.permissions import IsAdminUser

class pagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'


class CreateTAG (generics.CreateAPIView):
    queryset = models.TAG.objects.all()
    serializer_class = serializers.Tag
    permission_classes = [IsAdminUser]


class AddCourse (generics.CreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['id']
    permission_classes = [IsAdminUser]

class GetCourse (generics.ListAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['id','url']
    ordering_fields  = ['score']
    pagination_class = pagination
    permission_classes = [IsAdminUser]

class UpdateCourse (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

class AddTeacher (generics.CreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.Teacher
    permission_classes = [IsAdminUser]


class AddCourseTag(generics.CreateAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.CourseTag
    permission_classes = [IsAdminUser]

class UpdateCourseTag (generics.RetrieveUpdateDestroyAPIView):
    queryset = models.CourseTAG.objects.all()
    serializer_class = serializers.CourseTag
    permission_classes = [IsAdminUser]
    lookup_field="id"

class AddCourseTeacher(generics.CreateAPIView):
    queryset = models.TeacherMakeCourse.objects.all()
    serializer_class = serializers.TeachersCourse
    permission_classes = [IsAdminUser]

class UpdateCourseTeacher(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.Teacher
    lookup_field = 'name'
    permission_classes = [IsAdminUser]


class PublishCourse(generics.CreateAPIView):
    queryset = models.Publish.objects.all()
    serializer_class = serializers.PublishCourse
    permission_classes = [IsAdminUser]

class UpdatePublishCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publish.objects.all()
    serializer_class = serializers.PublishCourse
    lookup_field = 'course'
    permission_classes = [IsAdminUser]

class UpdatePublisher(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.Publisher
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

class CreateUser(generics.CreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]
