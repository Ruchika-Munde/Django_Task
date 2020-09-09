from django.urls import path
from . import views
urlpatterns=[

    path('display/',views.display_view),
    path('add/<int:id>/',views.add_view),

]