# Generated by Django 3.1.6 on 2021-05-31 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0002_auto_20210529_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='cr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='students',
        ),
    ]