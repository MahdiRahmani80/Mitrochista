# Generated by Django 4.0.5 on 2022-06-28 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_clickcourse_publisher_alter_clickcourse_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 274937)),
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 263583)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 270597)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 274072)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 275852)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 270155)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 264439)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 272479)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 28, 19, 34, 36, 275444)),
        ),
    ]
