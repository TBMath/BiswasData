# Generated by Django 2.1 on 2021-09-11 11:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fmembers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]