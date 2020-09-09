from django.contrib import admin
from FirstApp.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['Name','Company','Salary','Experience']

admin.site.register(Employee,EmployeeAdmin)