# Generated by Django 4.0.5 on 2022-07-03 12:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_publisher_password_alter_course_addtime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='addTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 109380)),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 116389)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 119827)),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='connectionWay',
            field=models.CharField(help_text='email or phone', max_length=600, unique=True),
        ),
        migrations.AlterField(
            model_name='searchlog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 121642)),
        ),
        migrations.AlterField(
            model_name='teachermakecourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 115929)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 110166)),
        ),
        migrations.AlterField(
            model_name='usersearchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 118190)),
        ),
        migrations.AlterField(
            model_name='watchcourse',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 3, 17, 2, 57, 121228)),
        ),
        migrations.CreateModel(
            name='Payment_IDPAY',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stp1DataReseveIDPAY', models.TextField(blank=True, null=True)),
                ('stp2DataReseveIDPAY', models.TextField(blank=True, null=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.publisher')),
            ],
        ),
    ]
