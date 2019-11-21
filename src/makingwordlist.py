import MeCab #単語分解に使用

def makig_word_list(str):
    #単語分類のための関数
    word_list = []
    mecab = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
    text = str

    mecab.parse('')#文字列がGCされるのを防ぐ
    node = mecab.parseToNode(text)
    while node:
        #単語を取得
        word = node.surface
        #print(word)
        word_list.append(word) #取得した単語をリストに入れる
        #次の単語に進める
        node = node.next
    return word_list
