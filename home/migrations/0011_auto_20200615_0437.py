# Generated by Django 3.0.6 on 2020-06-15 04:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200615_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 15, 4, 37, 10, 453406, tzinfo=utc), verbose_name='date joined'),
        ),
    ]