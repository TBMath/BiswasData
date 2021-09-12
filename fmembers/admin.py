from django.contrib import admin
from . import models

class GrowthAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "date_created")
    exclude = ("date_created",)
# Register your models here.
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Growth, GrowthAdmin)