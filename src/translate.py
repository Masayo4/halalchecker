from googletrans import Translator #日本語=>英語 の翻訳に使用

def jpn_to_eng_translate(jpn_list):
    jpn_words_list = jpn_list
    eng_words_list = []
    for word in jpn_words_list:
        translator = Translator()
        #print(translator.translate(word)) #第２引数にdest="ja"などで言語指定可能
        #Translated(src=ja, dest=en, text=Good morning, pronunciation=None, extra_data="{'translat...") 出力フォーマット
        #print(translator.translate(word).text) #.textでワードのみの取り出し
        translated_word = translator.translate(word).text
        eng_words_list.append(translated_word)

    return eng_words_list
