bot_talk = {'こんにちわ':'ハイ！コンニチワ。ナイカゴヨウデスカ？','会社概要を確認したいです':'コチラデイカガデショウカ？http://isc21.co.jp/info/gaiyou.html','ありがとうございます':'マタノゴリヨウオマチシテオリマス。'}
while True:
    command = input('bot> ')
    responce = ""
    # 辞書のキーが含まれているかチェックする
    for key in bot_talk:
        if key in command:
            responce = bot_talk[key]
            break
    # 辞書に登録がなければ空文字で返すので判定される
    if not responce:
        responce = 'スミマセン！ワカリマセン。'
    print(responce)
    if 'さよなら' in command:
        break