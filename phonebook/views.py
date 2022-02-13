from django.shortcuts import render
from .models import Contact


def add(request):
    return render(request, 'phonebook/add.html', context={})


def delete(request, post_id):
    return render(request, 'phonebook/delete.html', context={})


def index(request):
    return render(request, 'phonebook/index.html', context={})


def get_data():
    contacts = Contact.objects.all()
    return contacts
