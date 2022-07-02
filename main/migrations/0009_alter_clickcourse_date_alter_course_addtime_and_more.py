# Generated by Django 4.0.5 on 2022-06-22 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_clickcourse_date_alter_course_addtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 292394)),
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 280713)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 288108)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 291549)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 293275)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 287663)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 281624)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 289950)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 22, 16, 45, 52, 292855)),
        ),
    ]
