# Generated by Django 3.1.3 on 2021-12-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_remove_newspostform_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navlist',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
