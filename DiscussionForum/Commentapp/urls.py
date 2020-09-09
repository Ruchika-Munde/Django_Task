from django.urls import path
from Commentapp import views
urlpatterns = [
    path('addcomment/<int:id>/',views.Addcomment.as_view()),
    # path('showcomment/',views.Showcomment.as_view()),
]