# Generated by Django 4.1.2 on 2022-10-27 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_last_activity_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_activity_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
