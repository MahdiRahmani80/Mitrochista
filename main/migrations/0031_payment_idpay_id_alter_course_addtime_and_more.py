# Generated by Django 4.0.5 on 2022-07-03 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_remove_payment_idpay_publisher_remove_payment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='idpay_id',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 528489)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 535376)),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 540139)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 534936)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 529301)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 537147)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 25, 24, 539739)),
        ),
    ]