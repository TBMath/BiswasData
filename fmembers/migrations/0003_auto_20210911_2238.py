# Generated by Django 2.1 on 2021-09-11 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmembers', '0002_person_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='growth',
            old_name='Growth',
            new_name='growth',
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
