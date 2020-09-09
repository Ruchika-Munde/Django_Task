from django.urls import path
from . import views
urlpatterns=[
    path('form_view/',views.view),
    path('form_display/',views.display),
    path('form_delete/<int:id>/',views.delete),
    path('form_update/<int:id>/',views.update)
]