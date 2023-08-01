
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES
        fp = file.get("file")
        name = fp.name
        dir = "/home/pengbo/code/python/dffmpeg/video"
        file_path = os.path.join(dir, name)
        ok = os.path.exists(dir)
        if not ok:
            os.makedirs(dir)
        with open(file_path, 'wb+') as f:
            for chunk in fp.chunks():
                f.write(chunk)
        return HttpResponse("upload success")
    else:
        return HttpResponse("file is none")