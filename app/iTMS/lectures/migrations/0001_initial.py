# Generated by Django 3.1.6 on 2021-05-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=30)),
                ('starts_at', models.TimeField()),
                ('ends_at', models.TimeField()),
                ('day', models.PositiveSmallIntegerField(choices=[(1, 'MONDAY'), (2, 'TUESDAY'), (3, 'WEDNESDAY'), (4, 'THURSDAY'), (5, 'FRIDAY'), (6, 'SATURDAY'), (7, 'SUNDAY')])),
            ],
        ),
    ]
