from django.contrib import admin
from .models import Framework,Language,Movies,Character
# Register your models here.
admin.site.register(Framework)
admin.site.register(Language)
admin.site.register(Movies)
admin.site.register(Character)