# Generated by Django 3.2.1 on 2021-05-05 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keeper', '0002_activity_activity_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='activity_end',
            field=models.TimeField(auto_now_add=False, default=datetime.datetime.now()),
            preserve_default=False,
        ),
    ]
