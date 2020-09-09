from django.urls import path
from Firstapp import views
urlpatterns=[
    path('show/',views.show),
    path('addimage/',views.addimage)
]