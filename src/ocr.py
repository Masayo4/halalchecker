#!/usr/bin/python
#coding:utf-8
import base64
import json
from requests import Request, Session
from bs4 import BeautifulSoup


def recognize_captcha(str_image_path):
        bin_captcha = open(str_image_path, 'rb').read()

        #str_encode_file = base64.b64encode(bin_captcha)
        str_encode_file = base64.b64encode(bin_captcha).decode("utf-8")

        str_url = "https://vision.googleapis.com/v1/images:annotate?key="

        str_api_key = "APIkey"


        str_headers = {'Content-Type': 'application/json'}

        str_json_data = {
            'requests': [
                {
                    'image': {
                        'content': str_encode_file
                    },
                    'features': [
                        {
                            'type': "TEXT_DETECTION",
                            'maxResults': 10
                        }
                    ]
                }
            ]
        }

        print("begin request")
        obj_session = Session()
        obj_request = Request("POST",
                              str_url + str_api_key,
                              data=json.dumps(str_json_data),
                              headers=str_headers
                              )
        obj_prepped = obj_session.prepare_request(obj_request)
        obj_response = obj_session.send(obj_prepped,
                                        verify=False,
                                        timeout=60,
                                        )
        print("this")
        print("end request")

        if obj_response.status_code == 200:
            #print (obj_response.text)
            with open('data.json', 'w') as outfile:
                json.dump(obj_response.text, outfile)
            return obj_response.text
        else:
            return "error"

if __name__ == '__main__':
    path = "images/test_label_pork.jpg"
    data = json.loads(recognize_captcha(path))
    data = data["responses"]
    print(data)
    for i in data:
        print(i["fullTextAnnotation"]["text"])
