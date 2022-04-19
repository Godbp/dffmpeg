import os.path

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        file = request.files
        fp = file.get("file")
        name = fp.filename
        dir = "/home/pengbo/code/python/dffmpeg/video"
        file_path = os.path.join(dir, name)
        ok = os.path.exists(dir)
        if not ok:
            os.makedirs(dir)
        fp.save(file_path)
        return HttpResponse("upload success")
    else:
        return HttpResponse("file is none")