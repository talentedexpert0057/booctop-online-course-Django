# Generated by Django 3.0.6 on 2020-06-22 16:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20200623_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 16, 53, 16, 706020, tzinfo=utc), verbose_name='date joined'),
        ),
    ]