from django.urls import path

from Firstapp import views

urlpatterns=[
    path('display/',views.display_view),
    path('add/',views.add_view),
    path('update/<int:id>/',views.update_view),
    path('delete/<int:id>/',views.delete_view),
]