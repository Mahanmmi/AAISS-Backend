# Generated by Django 3.0.7 on 2020-07-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0005_auto_20200708_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='fields_of_interest',
            field=models.ManyToManyField(blank=True, to='backend_api.FieldOfInterest'),
        ),
    ]
