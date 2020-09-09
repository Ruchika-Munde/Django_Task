from django.contrib import admin
from .models import Mobile

# Register your models here.
class MobileAdmin(admin.ModelAdmin):
    list_display=['Brand','ModelName','Price','Ram']

admin.site.register(Mobile , MobileAdmin)

