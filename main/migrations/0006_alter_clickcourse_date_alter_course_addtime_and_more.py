# Generated by Django 4.0.5 on 2022-06-18 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_clickcourse_date_alter_course_addtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clickcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 735728)),
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 724235)),
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.CharField(default='<function uuid4 at 0x7f82cf2ada20>', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 730006)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 734786)),
        ),
        migrations.AlterField(
            model_name='publish',
            name='id',
            field=models.CharField(default='<function uuid4 at 0x7f82cf2ada20>', editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 736664)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 729557)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 724742)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 732436)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 18, 12, 59, 47, 736248)),
        ),
    ]
