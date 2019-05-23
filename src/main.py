import base64
import json
from requests import Request,Session
from bs4 import BeautifulSoup


import sys

import ssss


def recognize_captcha(str_image_path):
        bin_captcha = open(str_image_path, 'rb').read()

        str_encode_file = base64.b64encode(bin_captcha).decode("utf-8")

        str_url = "https://vision.googleapis.com/v1/images:annotate?key="

        str_api_key = "[YOUR_APIKEY]"
        #gitにあげるときは取り除く

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
                                        verify=True,
                                        timeout=60
                                        )
        print("end request")

        if obj_response.status_code == 200:
            #print (obj_response.text)
            with open('data.json', 'w') as outfile:
                json.dump(obj_response.text, outfile)
            return obj_response.text
        else:
            return "error"

def detect_haram_from_list(json_data,index,arr):
    for i in json_data:
        #print(i["fullTextAnnotation"]["text"])
        for j in range(len(i['textAnnotations'])):
            temp = i['textAnnotations'][j]['description']

            if len(temp) != 0:
                if index != True:
                    arr.append(temp)
                if not arr:
                    index = False
                    #print(list)
    #print(list) 取ってきたリストの確認
    #一度リストに落とし込んでからそのリストの中を判定しに行く

    #この下に判定基準の判別を書いていく

    pork_haram_counter =list.count('豚肉') #ex)豚肉の検出
    alcohol_haram_counter = list.count('酒')

    return pork_haram_counter, alcohol_haram_counter

def show_result(counter):
    pork_ele = counter[0]
    alcohol_ele = counter[1]
    counter = pork_ele + alcohol_ele
    if counter ==0:
        print("no pork,no alcohol.")
    else:
        if pork_ele == 0:
            print("no pork")
        else:
            print("this contain pork.")
        if alcohol_ele == 0:
            print("no alcohol")
        else:
            print("this contain alcohol.")

def init_all(arr,index):
    arr = arr.clear()
    index = True


if __name__ == '__main__':

    path = sys.argv[1]
    print(path)

    list = []
    first_index = True

    data = json.loads(recognize_captcha(path))
    data = data["responses"]

    haram_counter = detect_haram_from_list(data,first_index,list)
    #print(haram_counter)
    show_result(haram_counter)

    init_all(list,first_index)
