import csv #csvを扱う際に使用
import os #ファイルの存在を確認, osに依存する処理
import pandas as pd #2回目以降の書き込み処理
import datetime,time


def save_csv(jpn_list,eng_list):
    jpn_words_list = jpn_list
    eng_words_list = eng_list
    print("jpnlen:{},englen:{}".format(len(jpn_words_list),len(eng_words_list)))
    making_date = datetime.date.today()
    csv_filename = "./data/csv/"+making_date.strftime('%Y%m%d')+".csv"
    if not os.path.isdir("./data/csv"):
        os.mkdir("./data/csv")

    file_exist = os.path.exists(csv_filename)
    today = datetime.datetime.fromtimestamp(time.time())
    timestamp= today.strftime('%I:%M:%S%p')

    if file_exist == False:
        open(csv_filename,'w',encoding="utf_8_sig")
        with open(csv_filename,'w',encoding="utf_8_sig") as csv_file:
            fieldnames = ["日本語","English"] #列の指定
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for word_i in range(len(eng_words_list)):
                writer.writerow({'日本語': jpn_words_list[word_i], 'English': eng_words_list[word_i]})

    else:
        df = pd.read_csv(csv_filename)
        with open(csv_filename,'a',encoding="utf_8_sig") as csv_file:
            writer = csv.writer(csv_file,lineterminator='\n')
            writer.writerow(["",""])
            writer.writerow(["timestmp",timestamp])
            for word_i in range(len(jpn_words_list)):
                writer.writerow([jpn_words_list[word_i],eng_words_list[word_i]])
