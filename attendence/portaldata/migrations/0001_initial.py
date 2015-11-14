# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_absent', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Conducted_Classes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('instructor', models.CharField(max_length=30)),
                ('is_conducted', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coursename', models.CharField(max_length=50)),
                ('year', models.IntegerField(default=0)),
                ('sem', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('instructor', models.CharField(max_length=30)),
                ('course', models.ForeignKey(to='portaldata.Course')),
                ('room', models.ForeignKey(to='portaldata.ClassRoom')),
            ],
        ),
        migrations.CreateModel(
            name='Seating_Arrangement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seat', models.CharField(max_length=6)),
                ('course', models.ForeignKey(to='portaldata.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rollno', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='portaldata.Course')),
                ('student', models.ForeignKey(to='portaldata.Student')),
            ],
        ),
        migrations.AddField(
            model_name='seating_arrangement',
            name='student',
            field=models.ForeignKey(to='portaldata.Student'),
        ),
        migrations.AddField(
            model_name='conducted_classes',
            name='course',
            field=models.ForeignKey(to='portaldata.Course'),
        ),
        migrations.AddField(
            model_name='conducted_classes',
            name='room',
            field=models.ForeignKey(to='portaldata.ClassRoom'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='conductedclass',
            field=models.ForeignKey(to='portaldata.Conducted_Classes'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='portaldata.Student'),
        ),
    ]
