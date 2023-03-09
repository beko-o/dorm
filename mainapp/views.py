from .models import *
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.templatetags import i18n


# def index(request):
#     template = loader.get_template('MyApp/index.html')
#     context = {}
#     return HttpResponse(template.render(context, request))
# class MonthPostDetailView(DetailView):
#     pass


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        surname = request.POST['surname']
        gender = request.POST['gender']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        # room = request.POST['room']
        student = Student(name=name, surname=surname, gender=gender, email=email, phone_number=phone_number)
        student.save()

        return redirect('register')

    return render(request, 'register.html')

# def reserve_place(request):
#
#     if request.method == 'POST':
#         room = request.POST['room']
#         place = int(request.POST['place'])
#         reservation = Student(room=room, place=place)
#         reservation.save()
#         # return redirect('register')
#         return HttpResponse('Place reserved!')
#     else:
#         return HttpResponse('Invalid request method')

        


def visualforstudent_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'visualforstudent.html',{'dropdown':dropdown})

# def register_page(request):
#     dropdown = NavList.objects.all()
#     return render(request, 'register.html',{'dropdown':dropdown})

def about_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'about_us.html',{'dropdown':dropdown})



def gallery_page(request):
    dropdown = NavList.objects.all()
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'dropdown':dropdown,'gallery':gallery})

def contact_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'contact.html', {'dropdown':dropdown})

def calendar_page(request):
    dropdown = NavList.objects.all()
    return render(request, 'calendar.html',{'dropdown':dropdown})

def kz_page(request):

    return render(request, '')
def ru_page(request):

    return render(request, '')
def en_page(request):

    return render(request, '')