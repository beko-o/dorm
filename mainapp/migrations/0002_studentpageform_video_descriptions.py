# Generated by Django 3.1.3 on 2021-12-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentpageform',
            name='video_descriptions',
            field=models.TextField(default=None, max_length=255),
        ),
    ]