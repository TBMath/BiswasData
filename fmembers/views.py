from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 
from .models import Person, Growth

# Create your views here.
def index(request):
     person = Person.objects.all()
     growth = Growth.objects.all()
     return render(request, "index.html", {"person":person, "growth":growth})

def details(request, id):
     person = get_object_or_404(Person, pk=id)
     growth = Growth.objects.all()
     return render(request, "details.html", {"person":person, "growth":growth})
