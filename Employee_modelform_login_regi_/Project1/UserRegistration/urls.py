from django.urls import path
from UserRegistration import views
urlpatterns = [

    path('success/',views.success),
]