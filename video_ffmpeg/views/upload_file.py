import os.path

from django.shortcuts import render
from django.http import HttpResponse


def upload_file(request):
    if request.method == 'POST':
        file = request.FILES
        fp = file.get("file")
        name = fp.name
        upload_dir = "/home/pengbo/code/python/dffmpeg/video"
        file_path = os.path.join(upload_dir, name)
        ok = os.path.exists(upload_dir)
        if not ok:
            os.makedirs(upload_dir)
        with open(file_path, 'wb+') as f:
            for chunk in fp.chunks():
                f.write(chunk)
        return HttpResponse("upload success")
    else:
        return HttpResponse("file is none")
