def makig_str(json_data,index):
    str  = ""
    #取ってきたデータを加工して表示する部分
    for i in json_data:
        for j in range(len(i['textAnnotations'])):
            temp = i['textAnnotations'][j]['description']
            if len(temp) != 0:
                if index == True:
                    index = False
                    #一番最初の要素だけ処理を行わない
                elif index != True:
                    str = str+temp
                    #一番最初以外は,全て文字列をくっつけて一つの塊にする
    return str #全部の文字が塊で返ってくる
