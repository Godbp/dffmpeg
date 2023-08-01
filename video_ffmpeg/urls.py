from video_ffmpeg.views.upload_file import upload_file
from video_ffmpeg.views.move_to_gif import to_gif

from django.urls import path

app_name = 'video'

urlpatterns = [
    path('upload', upload_file),
    path('to_gif', to_gif),
]

