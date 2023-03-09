from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.
class NewsAdmin(TranslationAdmin):
    prepopulated_fields = {'slug':('title',)}  


admin.site.register(SwiperImg)

admin.site.register(NavList)


admin.site.register(Gallery)
