# Generated by Django 3.2.1 on 2021-05-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keeper', '0006_activity_activity_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_duration',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
