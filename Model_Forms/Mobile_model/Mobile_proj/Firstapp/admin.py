from django.contrib import admin
from Firstapp.models import Mobile
# Register your models here.

class MobileAdmin(admin.ModelAdmin):
    list_display = ['Brand','Mname','Price','Ram']

admin.site.register(Mobile,MobileAdmin)