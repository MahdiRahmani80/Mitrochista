# Generated by Django 4.0.5 on 2022-06-22 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_clickcourse_date_alter_course_addtime_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursetag',
            name='course',
        ),
        migrations.RemoveField(
            model_name='coursetag',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='coursetag',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='coursetag',
            name='tag',
        ),
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 512435)),
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 492590)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 504413)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 510994)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 514069)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 503580)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 494146)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 507993)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 19, 52, 22, 513256)),
        ),
    ]