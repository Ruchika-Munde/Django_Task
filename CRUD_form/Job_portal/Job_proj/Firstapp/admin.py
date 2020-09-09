from django.contrib import admin
from .models import privatejob
# Register your models here.
class privateAdmin(admin.ModelAdmin):
    list_display = ['padd1','padd2','padd3','padd4','padd5','padd6']

admin.site.register(privatejob,privateAdmin)