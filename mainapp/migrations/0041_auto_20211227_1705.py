# Generated by Django 3.1.3 on 2021-12-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0040_auto_20211227_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clubs_page_form',
            name='img',
        ),
        migrations.AddField(
            model_name='clubs_page_form',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]