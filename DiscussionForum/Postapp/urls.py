from django.urls import path
from Postapp import views
urlpatterns = [
    path('addpost/',views.Addpost.as_view()),
    path('showpost/',views.posttitle.as_view()),
    path('postdetail/<int:id>/',views.postdetails.as_view()),
    path('base/',views.base.as_view()),
]