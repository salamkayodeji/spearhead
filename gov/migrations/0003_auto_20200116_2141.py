# Generated by Django 3.0.2 on 2020-01-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gov', '0002_auto_20200116_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='course_slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='null', max_length=200),
        ),
    ]