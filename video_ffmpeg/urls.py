from video_ffmpeg.views.upload_file import upload_file

from django.urls import path

app_name = 'video'

urlpatterns = [
    path('upload', upload_file),
]

