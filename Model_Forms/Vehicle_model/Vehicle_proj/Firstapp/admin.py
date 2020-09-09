from django.contrib import admin
from Firstapp.models import Vehicle
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['Brand','Model','Price','Average']

admin.site.register(Vehicle,VehicleAdmin)