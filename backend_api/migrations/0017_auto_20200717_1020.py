# Generated by Django 3.0.7 on 2020-07-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0016_auto_20200717_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenter',
            name='paper',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='presenter',
            name='workplace',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='pic',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
