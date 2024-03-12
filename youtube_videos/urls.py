from . import views
from django.urls import path

app_name='youtube_videos'
urlpatterns=[
   path('', views.VideotList.as_view()),
   path('search/', views.VideoSearchView.as_view())
]
