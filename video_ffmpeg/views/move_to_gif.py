import os

from django.http import HttpResponse
from moviepy.editor import VideoFileClip


def to_gif(request):
    if request.method == 'POST':
        file = request.FILES
        fp = file.get("file")
        name = fp.name
        upload_dir = "/Users/pengbo/Desktop/projects/git-project/dffmpeg/upload_file"
        file_path = os.path.join(upload_dir, name)
        out_path = os.path.join(upload_dir, "result.gif")
        ok = os.path.exists(upload_dir)
        if not ok:
            os.makedirs(upload_dir)
        with open(file_path, 'wb+') as f:
            for chunk in fp.chunks():
                f.write(chunk)
        video_to_gif(file_path, out_path, 10)
        return HttpResponse("ok")


def video_to_gif(input_file, output_file, fps=10, duration=None):
    # 打开视频文件
    video_clip = VideoFileClip(input_file)

    # 如果未指定持续时间，则使用视频的全部时长
    if duration is None:
        duration = video_clip.duration

    # 将视频转换为 GIF
    gif_clip = video_clip.subclip(0, duration)
    gif_clip.write_gif(output_file, fps=fps)



