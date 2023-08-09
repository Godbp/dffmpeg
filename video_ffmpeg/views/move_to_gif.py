import os
import time
import asyncio

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


def constant_time_compare(v1, v2):
    if len(v1) != len(v2):
        return False
    result = 0
    for x, y in zip(v1, v2):
        result |= ord(x) ^ ord(y)
    return result == 0


def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # 初始化增量，也可以选择其他增量序列

    while gap > 0:
        # 对每个子列表进行插入排序
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # 插入排序
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2  # 缩小增量


async def sleep_print(t: float):
    print("async start ------", t)
    await asyncio.sleep(t)
    print("async end ------", t)


def start():
    l = [11, 10, 9, 8, 7, 6]

    task = []
    for i in l:
        task.append(sleep_print(i))

    tl = time.time()

    asyncio.run(asyncio.wait(task))
    print("end: ", time.time() - tl)

start()
