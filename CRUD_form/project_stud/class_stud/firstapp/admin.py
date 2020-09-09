from django.contrib import admin
from firstapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['Name','Rollno','Marks','Address']
admin.site.register(Student,StudentAdmin)