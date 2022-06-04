# Generated by Django 3.2.13 on 2022-05-31 04:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20220531_0829'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='indexCoder',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 584218)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 579849)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 583314)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 585391)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 579378)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 573872)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 581673)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 8, 35, 19, 584887)),
        ),
    ]
