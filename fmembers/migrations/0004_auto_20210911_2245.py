# Generated by Django 2.1 on 2021-09-11 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmembers', '0003_auto_20210911_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='growth',
            name='growth',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=13300),
        ),
    ]