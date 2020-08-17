from django.shortcuts import render, HttpResponse
from Home import models

# Create your views here.

def home(request):
    context = {'name': 'Avi', 'website': 'Portfolio'}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def projects(request):
    return render(request, 'projects.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = models.Contacts(name=name, email=email, phone=phone, desc=desc)
        ins.save()
      #  print("data is written successfully")

    return render(request, 'contacts.html')
