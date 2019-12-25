#coding:utf-8
import json
import requests
class MyRequests():
    def __init__(self, method, url, data=None, headers=None):
        self.method = method
        self.url = url
        self.data = data
        self.headers = headers
    def myrequests(self):
        if self.method == "post":
            if self.data != None:
                res = requests.post(self.url, data = self.data.encode(), headers = self.headers)
            else:
                res = requests.post(self.url, headers = self.headers)
        elif self.method == "get":
            res = requests.get(self.url, headers = self.headers)
        else:
            return -1
        return res.json()
if __name__ == "__main__" and __package__ is None:
    __package__ = "myrequests"

if __name__ == "__main__":
    #data = '{"name": "OTT流畅", "content": {"format": "MP4", "vCodec": "h264", "vBitrate": "380k","vResolution": "360*270", "vFps": 25, "aCodec": "AAC", "aBitrate": "50", "aSampleRate": 44100 },"use_watermark": false }'
    #data = json.loads(data)
    data = None
    url = "http://10.200.11.40:8081/api/v2/trans/mt/list?name=mtTest"
    method = "get"
    headers = {"domain":"transsvc-82fb7515d1ce9cd45697b3cf11111111", "Content-Type":"application/json"}
    res = MyRequests(method, url, data=data, headers=headers).myrequests()
    print(res)
