from django.contrib import admin
from . import models

class GrowthAdmin(admin.ModelAdmin):
    list_display = ("id", "growth")

class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "growth")
    exclude = ("date_created",)
# Register your models here.
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Growth, GrowthAdmin)