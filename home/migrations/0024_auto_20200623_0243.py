# Generated by Django 3.0.6 on 2020-06-22 16:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20200620_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 16, 43, 49, 172837, tzinfo=utc), verbose_name='date joined'),
        ),
    ]
