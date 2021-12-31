from django.shortcuts import render
from django.http import HttpResponse
import random
import names
# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'dfij39sdfn3'})

def password(request):
    
    

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special characters'):
        characters.extend('!@#$%^&*')
    
    if request.GET.get('numbers'):
        characters.extend('0123456789')

    length = int(request.GET.get('length' , 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')

def name(request):
    
    gender = request.GET.get('gender')
    
    if gender=='Girl':
        thename = names.get_first_name(gender='female')
    if gender=='Boy':
        thename = names.get_first_name(gender='male')
    
    return render(request, 'generator/name.html', {'name': thename})

