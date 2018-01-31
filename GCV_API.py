#usr/bin/python
#encoding:utf-8
import base64
import json
import sys
import codecs
from requests import Request,Session
# Cloud Vision APIで画像を分析
# CAPTCHAの分析
def recognize_captcha(str_image_path):
    #CAPTCHA画像の読み込み
    bin_captcha = open(str_image_path,'rb').read()
    # base64でCAPTCHA画像をエンコード
    str_encode_file = base64.b64encode(bin_captcha)
    # APIのURLを指定
    str_url = "https://vision.googleapis.com/v1/images:annotate?key="
    # 事前に取得したAPIキー
    str_api_key = "AIzaSyCs0X-UOq8JKZ0h4eKxtTspK4SqhT58lUU"
    # Content-TypeをJSONに設定
    str_headers = {'Content-Type':'application/json'}
    # Cloud Vision APIの仕様に沿ってJSONのペイロードを定義。
    # CAPTCHA画像からテキストを抽出するため、typeは「TEXT_DETECTION」にする。
    str_json_data={'requests':[{
                        'image':{'content':str_encode_file},
                        'features':[{'type':"TEXT_DETECTION",'maxResults':10}]
                   }]
    }
    #リクエスト送信
    #print("begin request")
    obj_session = Session()
    obj_request = Request("POST",
                          str_url+str_api_key,
                          data=json.dumps(str_json_data),
                          headers=str_headers
    )
    obj_prepped = obj_session.prepare_request(obj_request)
    obj_response = obj_session.send(obj_prepped,verify=True,timeout=60)
    #print("end request")
    # 分析結果の取得
    if obj_response.status_code == 200:
         #print obj_response.text
         with open('data.json', 'w') as outfile:
             json.dump(obj_response.text, outfile)
         return obj_response.text
    else:
         return "error"
def cutting_out():
    f = open('data.json','r')
    json1=json.loads(json.load(f))
    #print('file:{}'.format(type(json1)))
    result = (u'{}'.format(json1['responses'][0]['fullTextAnnotation']['text']))
    print('読み取り結果:')
    #print(result)
    f2 = codecs.open('result.txt', 'w', 'utf-8')
    f2.write(result)
    f2.close()
if __name__ == '__main__':
    if len(sys.argv) <= 1:
          print("[USAGE] findfile (image_file)")
          sys.exit(0)
    image_file = sys.argv[1]
    recognize_captcha(image_file)
    cutting_out()


