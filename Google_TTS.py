import json
import urllib2
import base64
import record
import os

def decode(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()
        
#Please repleace your API_key in the next line.
api_url = "https://texttospeech.googleapis.com/v1beta1/text:synthesize?key=your_API_key"
tts_text="how are you?"
voice = {
  "audioConfig": {
    "audioEncoding": "MP3",
    "pitch": "0.00",
    "speakingRate": "1.00"
  },
  "input": {
    "text":tts_text
  },
  "voice": {
    "languageCode": "en-US",
    "name": "en-US-Wavenet-D"
  }
}

headers = {'Content-Type': 'application/json'}
request = urllib2.Request(url=api_url, headers=headers, data=json.dumps(voice))
response = urllib2.urlopen(request)
response_str = response.read().decode('utf8')
response_dic = json.loads(response_str)
cont=response_dic['audioContent']
with open('tts.txt','w') as tt:
  tt.write(cont)
decode('tts.txt',"tts.mp3")
#print(response.read()['audioContent'])

