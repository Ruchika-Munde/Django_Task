from django.contrib import admin
from Userapp.models import User
# Register your models here.
class useradmin(admin.ModelAdmin):
    list_display=['name','username','password','confirm_password','email','gender','tag']


admin.site.register(User,useradmin)