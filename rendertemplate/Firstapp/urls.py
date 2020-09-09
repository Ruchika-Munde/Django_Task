from django.urls import path
from Firstapp import views
urlpatterns=[
    path('add/',views.Add),
    path('show/',views.Show)

]