from video_ffmpeg import views

from django.urls import path

app_name = 'video'

urlpatterns = [
    path('/upload', views.upload_file),
]

