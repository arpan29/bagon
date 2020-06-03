# Generated by Django 2.2.10 on 2020-06-03 12:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.FloatField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('facility_id', models.IntegerField(default=0)),
                ('vehicle_type', models.CharField(default='', max_length=255)),
                ('total_slots', models.IntegerField(default=0)),
                ('available_slots', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('facility_id', models.IntegerField(default=0)),
                ('vehicle_type', models.CharField(default='', max_length=255)),
                ('start_time', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59))),
                ('end_time', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59))),
                ('amount', models.FloatField(max_length=255)),
                ('reg_no', models.CharField(default='', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
