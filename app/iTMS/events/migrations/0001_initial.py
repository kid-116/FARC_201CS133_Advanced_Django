# Generated by Django 3.1.6 on 2021-05-30 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sections', '0002_auto_20210529_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('starts_at', models.DateTimeField()),
                ('ends_at', models.DateTimeField()),
                ('venue', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=300, verbose_name='Description')),
                ('section', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='sections.section')),
            ],
        ),
    ]
