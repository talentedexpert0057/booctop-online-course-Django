# Generated by Django 3.0.6 on 2020-06-15 04:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200615_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_categories',
            name='user',
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 15, 4, 26, 5, 487473, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AlterField(
            model_name='user_categories',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
