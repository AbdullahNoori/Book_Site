# Create your views here.
from django.shortcuts import render
from .models import *


def home(request):
  context = {
      'books': Book.objects.all()
  }
  return render(request, 'home.html', context)

def detail(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'detail.html', context)