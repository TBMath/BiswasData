from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

# Create your views here.
# def index(request):
#      person = Person.objects.all()
#      return render(request, "index.html", {"Person":person})
def index(requests):
     person = Person.objects.all()
     return render(requests, "index.html", {"person":person})

