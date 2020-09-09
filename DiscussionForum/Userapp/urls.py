from django.urls import path
from Userapp import views
urlpatterns = [
    path('user_reg/',views.UserRegistration.as_view()),
    path('user_login/',views.UserLogin.as_view()),
]