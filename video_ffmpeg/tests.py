from django.test import TestCase

# Create your tests here.

import requests

def test_upload_video():
    url = 'http://127.0.0.1:8000/upload'
    files = {'file': open('home/pengbo/视频/001.mp4', 'rb')}

    response = requests.post(url, files=files, data=data)
    json = response.json()
    print(json)
