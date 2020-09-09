from django.urls import path
from . import views
urlpatterns=[
    path('display/',views.display_view),
    path('top/',views.top_news),
    path('trend/',views.trending_news),
    path('politics/',views.politics_news),
]