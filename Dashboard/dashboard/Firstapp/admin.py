from django.contrib import admin
from Firstapp.models import Address,ITJobs,MECHJobs,CIVILJobs
# Register your models here.

admin.site.register(Address)
admin.site.register(ITJobs)
admin.site.register(MECHJobs)
admin.site.register(CIVILJobs)