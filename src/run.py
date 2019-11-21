#flask周りのimport
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
#moduleimport
import numpy as np #imgのuploadで使用

import cv2
from datetime import datetime
import os
import string
import random
import json

#以下自作関数
from halalcheckerinit import halal_checker_init
from ocr import recognize_captcha
from makingstr import makig_str
from makingwordlist import makig_word_list
from translate import jpn_to_eng_translate
from savecsv import save_csv

app = Flask(__name__)

SAVE_DIR = "images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)

@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)

        # 保存
        dt_now = datetime.now().strftime("%Y_%m_%d%_H_%M_%S_") + random_str(5)
        save_path = os.path.join(SAVE_DIR, dt_now + ".png")
        cv2.imwrite(save_path, img)

        print("save", save_path)
        # ここでOCRを呼ぶ
        japanese_word_list = []
        english_words_list = []
        json_data = json.loads(recognize_captcha(save_path))
        perth_data = json_data["responses"]
        first_index = True #一番最初のデータには触らない(データの形が扱いにくい)
        detect_str = makig_str(perth_data,first_index)
        japanese_word_list = makig_word_list(detect_str)
        print(japanese_word_list) #word_listのデバック
        english_words_list = jpn_to_eng_translate(japanese_word_list)
        print(english_words_list) #translate_listのデバッグ

        save_csv(japanese_word_list,english_words_list)
        halal_checker_init()
        return redirect('/')

@app.route('/')
def index():
    #halal_checker_init()
    return render_template('index.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8888)
