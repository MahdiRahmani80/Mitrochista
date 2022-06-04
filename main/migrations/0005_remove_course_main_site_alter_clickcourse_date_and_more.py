# Generated by Django 4.0.2 on 2022-05-26 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_user_name_alter_clickcourse_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='main_site',
        ),
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 903363)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 898142)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 902598)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 904240)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 897683)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 894064)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 900025)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 26, 4, 0, 0, 903833)),
        ),
    ]
