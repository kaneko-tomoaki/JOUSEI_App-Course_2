import PySimpleGUI as sg

#1.レイアウトの作成 　このエリアで、ウィンドウ内に表示し続ける文字や数値を入力して、ウィンドウの「枠組み」を作る。

layout = [[sg.Text("1つ目の数字を入力"), sg.InputText(key='-入力1-', size=(5, 1))],
           [sg.Text("2つ目の数字を入力"), sg.InputText(key='-入力2-', size=(5, 1))],
           [sg.Button("計算"), sg.Button("リセット")],
           [sg.Text('入力した数字の合計値',key='合計'), sg.Text(key='-出力-')]
]

#2.ウィンドウの生成

window = sg.Window('順次構造',layout,grab_anywhere=True)

#3.ウィンドウの表示　

# eventは、 ユーザーの操作によって起きた出来事を収めた変数。
# valuesは、その出来事についての情報（キーと値）を収めた「辞書」を収めた変数。
while True:
    event,values = window.read() #window.read()というメソッドは、1.画面でどんな出来事が起きたか、それによってどんな値が生成されたかを教えてくれる。
                                 #起きた出来事の情報は変数eventに、結果として生成された値は変数valuesに格納する。

#3.ウィンドウを閉じる

    if event == sg.WIN_CLOSED: # 画面の閉じるボタンが押されたら
        break                  # ウィンドウを閉じて、プログラム終了。 
          
    if event == '計算':         #「計算」ボタンが押されたら、
        try:
            数値1 = int(values['-入力1-']) #「辞書」からキー(入力１）を使って値(value)を取り出して、変数数値1に入れる。
            数値2 = int(values['-入力2-']) #「辞書」からキー(入力２）を使って値(value)を取り出して、変数数値2に入れる。
            result = 数値1 + 数値2         #　合計を行い、
            window['-出力-'].update(f"{result}です。") # 結果を表示する。
        except ValueError:
            sg.popup_error('無効な入力です。数値を入力してください。') # 入力が半角の数字出なかった場合は、メッセージを表示して、再入力を促す。

    if event == 'リセット':# リセットボタンが押されたらwindow内の値を消す。
        window['-入力1-'].update('')
        window['-入力2-'].update('')
        window['-出力-'].update('')

#windowをクローズし終了

window.close() 

