from django.urls import path
from . import views
urlpatterns = [
        path('index',views.index),
        path('display/',views.display_view)
    ]