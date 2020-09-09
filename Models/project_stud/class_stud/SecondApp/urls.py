from django.urls import path
from . import views
urlpatterns = [
    path('display/',views.display),
    path('add1/',views.add),
    path('delete1/<int:id>/',views.delete) ,#id  is same name as views.py in delete(id)
    path('update1/<int:id>/',views.update) #id  is same name as views.py in update(id)
    ]