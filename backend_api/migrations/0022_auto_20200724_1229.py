# Generated by Django 3.0.7 on 2020-07-24 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0021_misc_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='presenter',
            old_name='desc',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='desc',
            new_name='bio',
        ),
    ]
