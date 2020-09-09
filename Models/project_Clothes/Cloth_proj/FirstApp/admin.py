from django.contrib import admin
from .models import Clothes
# Register your models here.

class ClothesAdmin(admin.ModelAdmin):
    list_display = ['Catagory','Price','Pattern']

admin.site.register(Clothes,ClothesAdmin)