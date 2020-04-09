# Generated by Django 2.2.6 on 2020-04-09 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerDetails',
            fields=[
                ('SerialNumber', models.AutoField(primary_key=True, serialize=False)),
                ('CreatedAt', models.DateField(default=django.utils.timezone.now)),
                ('ipaddress', models.TextField(max_length=40)),
                ('hdd', models.TextField(max_length=30)),
                ('ram', models.TextField(max_length=30)),
                ('core', models.TextField(max_length=30)),
                ('allocatedFor', models.TextField(max_length=30)),
                ('creationOrder', models.TextField(max_length=30)),
                ('os', models.TextField(max_length=40)),
                ('License', models.TextField(max_length=60)),
            ],
        ),
    ]
