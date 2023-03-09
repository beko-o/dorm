from django.urls import path,include
from mainapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path('roomchoose/', register, name='roomchoose'),
    path('register/',register ,name = 'register'),
    path('visualforstudent/',visualforstudent_page ,name = 'visualforstudent'),
    path('', about_page ,name='about' ),

    path('gallery/',gallery_page , name='gallery'),
    path('contact/',contact_page , name='contact'),

    path('kz/' , kz_page , name = 'kzPage'),
    path('ru/' , ru_page , name = 'kzPage'),
    path('en/' , en_page , name = 'kzPage')
]

urlpatterns += staticfiles_urlpatterns()
