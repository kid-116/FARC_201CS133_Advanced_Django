# Generated by Django 3.1.6 on 2021-05-31 03:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='section',
        ),
    ]
