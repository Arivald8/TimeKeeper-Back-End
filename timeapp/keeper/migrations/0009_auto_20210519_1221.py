# Generated by Django 3.2.1 on 2021-05-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keeper', '0008_activity_activity_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='activity_start',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_duration',
            field=models.CharField(max_length=300),
        ),
    ]
