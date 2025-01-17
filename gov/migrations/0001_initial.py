# Generated by Django 3.0.2 on 2020-01-14 04:45

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='headshots/')),
                ('description', models.TextField(default='description')),
                ('coursename', models.CharField(blank=True, max_length=50, null=True)),
                ('slug', models.SlugField(null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=20, null=True)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('day', models.IntegerField()),
                ('month', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pic', models.ImageField(blank=True, null=True, upload_to='headshots/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=50)),
                ('amount', models.CharField(max_length=10)),
                ('content', ckeditor.fields.RichTextField(blank=True, default='content', null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='headshots/')),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('popular', models.BooleanField(blank=True, null=True)),
                ('venue_1', models.CharField(blank=True, max_length=200, null=True)),
                ('venue_2', models.CharField(blank=True, max_length=200, null=True)),
                ('venue_3', models.CharField(blank=True, max_length=200, null=True)),
                ('venue_4', models.CharField(blank=True, max_length=200, null=True)),
                ('subject_id', models.CharField(default='null', max_length=200)),
                ('slug', models.SlugField(null=True)),
                ('date_1', models.DateField(blank=True, null=True)),
                ('date_2', models.DateField(blank=True, null=True)),
                ('date_3', models.DateField(blank=True, null=True)),
                ('date_4', models.DateField(blank=True, null=True)),
                ('date_5', models.DateField(blank=True, null=True)),
                ('date_6', models.DateField(blank=True, null=True)),
                ('date_7', models.DateField(blank=True, null=True)),
                ('date_8', models.DateField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('coursecategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gov.Category')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
