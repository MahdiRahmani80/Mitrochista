# Generated by Django 4.0.5 on 2022-07-03 13:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_payment_idpay_id_alter_course_addtime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 203225)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 210653)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 215835)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 210166)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 204080)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 212569)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 30, 41, 215403)),
        ),
    ]