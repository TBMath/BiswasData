from django.db import models
from tastypie.resources import ModelResource
from fmembers.models import Person

# Create your models here.
class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = "fmembers"
        excludes = ["date_created"]