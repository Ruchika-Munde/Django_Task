from django.urls import path
from . import views
urlpatterns = [
    path('form_view/',views.view),
    path('form_delete/<int:id>/',views.delete),
    #path('form_update/<int:id>/',views.update),
    path('form_update/<int:id>/',views.update1),
    path('form_display/',views.display1),
    ]