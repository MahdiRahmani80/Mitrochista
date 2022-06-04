# Generated by Django 4.0.2 on 2022-05-26 04:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_course_main_site_alter_clickcourse_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 79960)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 74234)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='replay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.coursecomment'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 79119)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 80866)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 73756)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 70059)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 76126)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 9, 4, 80446)),
        ),
    ]
