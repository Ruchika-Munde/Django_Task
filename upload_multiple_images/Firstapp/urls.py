from django.urls import path
from Firstapp import views
urlpatterns = [
    path('upload/',views.uploadimage)
]