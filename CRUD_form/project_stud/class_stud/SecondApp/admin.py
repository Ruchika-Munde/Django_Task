from django.contrib import admin

# Register your models here.
from .models import Form
class FormAdmin(admin.ModelAdmin):
    list_display = ['Name']

admin.site.register(Form,FormAdmin)