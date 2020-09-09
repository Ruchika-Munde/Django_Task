from django.contrib import admin
from .models import Employee

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr','email']
admin.site.register(Employee,EmpAdmin)



# Register your models here.
