from django.db import models
from django.utils import timezone


# Create your models here.
class Growth(models.Model):
    growth = models.CharField(max_length=300)



class Person(models.Model): 
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    growth = models.ForeignKey(Growth, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)