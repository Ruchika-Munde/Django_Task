from django.urls import path
from . import views
urlpatterns = [

    path('display/',views.display),
    path('student/<int:id>/',views.Student.as_view()), # gives number
    #path('student/<slug:id>/',views.Student.as_view()), # gives a-z,0-9 not special character

]
