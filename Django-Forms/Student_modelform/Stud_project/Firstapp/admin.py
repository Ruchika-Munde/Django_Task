from django.contrib import admin
from  .models import Student
# Register your models here.

class StudAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','marks','addr']

admin.site.register(Student,StudAdmin)