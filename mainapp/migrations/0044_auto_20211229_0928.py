# Generated by Django 3.1.3 on 2021-12-29 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0043_valountervideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navlist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='navlist',
            name='description_second',
        ),
        migrations.RemoveField(
            model_name='newspostform',
            name='description',
        ),
        migrations.AddField(
            model_name='navlist',
            name='descriptionEN',
            field=models.TextField(default='', max_length=800, verbose_name=' Первый абзац на английском'),
        ),
        migrations.AddField(
            model_name='navlist',
            name='descriptionKZ',
            field=models.TextField(default='', max_length=800, verbose_name=' Первый абзац на казахском'),
        ),
        migrations.AddField(
            model_name='navlist',
            name='descriptionRU',
            field=models.TextField(default='', max_length=800, verbose_name=' Первый абзац на русском'),
        ),
        migrations.AddField(
            model_name='newsbigpost',
            name='descriptionEN',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='newsbigpost',
            name='descriptionRU',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='newslongpost',
            name='descriptionEN',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='newslongpost',
            name='descriptionRU',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='newspostform',
            name='descriptionEN',
            field=models.TextField(default='', max_length=900),
        ),
        migrations.AddField(
            model_name='newspostform',
            name='descriptionKZ',
            field=models.TextField(default='', max_length=900),
        ),
        migrations.AddField(
            model_name='newspostform',
            name='descriptionRU',
            field=models.TextField(default='', max_length=900),
        ),
        migrations.AddField(
            model_name='newsshortpost',
            name='descriptionEN',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='newsshortpost',
            name='descriptionRU',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='talapkerpost',
            name='descriptionEN',
            field=models.TextField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='talapkerpost',
            name='descriptionRU',
            field=models.TextField(default='', max_length=400),
        ),
    ]
