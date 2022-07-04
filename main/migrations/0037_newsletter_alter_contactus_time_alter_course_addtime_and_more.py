# Generated by Django 4.0.5 on 2022-07-04 10:43

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_delete_article_alter_contactus_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsLetter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='time',
            field=models.DateField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 818814)),
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 806173)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 813483)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 817069)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 818471)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 813043)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 807052)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 815311)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 4, 15, 13, 49, 818065)),
        ),
    ]