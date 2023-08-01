from django.test import TestCase

# Create your tests here.

import requests


def test_upload_video():
    url = 'http://127.0.0.1:8000/video/upload'
    files = {'file': open('/home/pengbo/001.mp4', 'rb')}

    response = requests.post(url, files=files)
    json = response.json()
    print(json)

def test_to_gif_test():
    url = 'http://127.0.0.1:8000/video/to_gif'
    files = {'file': open('/Users/pengbo/Desktop/屏幕录制2023-07-31 17.12.43.mov', 'rb')}

    response = requests.post(url, files=files)
    json = response.json()
    print(json)

if __name__ == "__main__":
    test_to_gif_test()