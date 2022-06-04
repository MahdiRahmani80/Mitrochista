# Generated by Django 4.0.2 on 2022-05-25 18:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=300)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('discription', models.TextField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=8000, null=True)),
                ('url', models.URLField(unique=True)),
                ('students', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('lang', models.CharField(max_length=50)),
                ('score', models.BigIntegerField(default=0)),
                ('main_site', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('state', models.IntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 191618))),
                ('comment', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('replay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coursecomment')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('price', models.BigIntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 195928))),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('SEORank', models.BigIntegerField(default=0)),
                ('LastIndexed', models.DateTimeField()),
                ('CreatedDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('search', models.CharField(max_length=200)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 197665))),
            ],
        ),
        migrations.CreateModel(
            name='SocalMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('platform', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TAG',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('score', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('ip', models.CharField(max_length=200)),
                ('score', models.IntegerField(default=0)),
                ('isVerified', models.BooleanField(default=False)),
                ('bio', models.CharField(max_length=300)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 187556))),
            ],
        ),
        migrations.CreateModel(
            name='WatchCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 197168))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserStarComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coursecomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserSocalMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.socalmedia')),
            ],
        ),
        migrations.CreateModel(
            name='UserSearchCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('search', models.CharField(blank=True, max_length=500, null=True)),
                ('count', models.BigIntegerField(default=0)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 193235))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserLikeComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coursecomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coursecomment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherSocalMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.socalmedia')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherMakeCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 191202))),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('tracher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='ReportPublisher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('msg', models.TextField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.publisher')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='ReportCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('msg', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='PublisherSocalMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.socalmedia')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_visible', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.payment')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('monney', models.BigIntegerField(default=5000)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.publisher')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTAG',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rank', models.BigIntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tag')),
            ],
        ),
        migrations.CreateModel(
            name='ClickCourse',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime(2022, 5, 25, 18, 42, 7, 196698))),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
