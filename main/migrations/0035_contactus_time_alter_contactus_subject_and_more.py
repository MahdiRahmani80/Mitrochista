# Generated by Django 4.0.5 on 2022-07-03 18:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_publisher_isup_alter_course_addtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='time',
            field=models.DateField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 948202)),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 935962)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 942949)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 946399)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 947862)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 942509)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 936785)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 944738)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 22, 33, 56, 947457)),
        ),
    ]