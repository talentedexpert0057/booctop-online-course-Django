# Generated by Django 3.0.6 on 2020-06-12 06:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200612_0506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 12, 6, 44, 52, 402331, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
