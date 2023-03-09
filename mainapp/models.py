from django.db import models
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.core.validators import RegexValidator, FileExtensionValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
# Create your models here.
from unidecode import unidecode


class Student(models.Model):
    name = models.CharField(max_length=100 , validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    surname = models.CharField(max_length=100 , validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=100 , validators=[MinLengthValidator(1), MaxLengthValidator(100)])
    phone_number = models.CharField(max_length=20 , validators=[MinLengthValidator(1), MaxLengthValidator(20)])
    # room = models.CharField(max_length=10, default=None)

    def save(self, *args, **kwargs):
        if self.name.strip() == "" or self.surname.strip() == "" or self.email.strip() == "" or self.phone_number.strip() == "":
            return  # do not save if any of the required fields is empty
        super().save(*args, **kwargs)
    # room = models.CharField(max_length=50, null=False, default='default_room_value')
    # place = models.IntegerField(null=False, default='')





class SwiperImg(models.Model):
    img = models.ImageField(upload_to="gallery")
    description = models.TextField(max_length=100, default='')


class SwiperVideo(models.Model):
    video = models.FileField(upload_to='videos_uploaded', null=True, validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])



class NavList(models.Model):
    title = models.CharField(max_length=20, default='')
    slug = models.SlugField(default='', unique=True)
    description = models.TextField(max_length=800, default='', verbose_name=' Первый абзац ')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NavList, self).save(*args, **kwargs)

    def __str__(self):
        return " {} ".format(self.title)



class Gallery(models.Model):
    img = models.ImageField(upload_to="gallery")

    title = models.CharField(max_length=20, default='')

    def __str__(self):
        return " {} ".format(self.title)

