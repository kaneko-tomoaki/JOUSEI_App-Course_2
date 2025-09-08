from rectangle_2 import 四角形の面積 #rectangle_2.pyから、関数「四角形の面積」をインポート
import PySimpleGUI as sg            #PySimpleGUIライブラリをインポート

layout = [[sg.Text('縦の長さ:'), sg.InputText(key = '-TATE-')], #　縦の長さを入力するテキストボックス　key = '-TATE-'は入力情報を後続のコードに知らせる目印
          [sg.Text('横の長さ:'), sg.InputText(key = '-YOKO-')], #　横の長さを入力するテキストボックス　key = '-TATE-'は入力情報を後続のコードに知らせる目印
          [sg.Button('計算')],                                  # 面積計算実行ボタン
          [sg.Text(key = '-OUTPUT-')]                           # 計算結果表示領域
         ]
window = sg.Window('四角形の面積',layout)                        # GUIウィンドウを表示

while True:                                                     # 無限ループを発生させ、
    event,values = window.read()                                # ユーザによるテキストボックスへの入力やボタンクリックといったイベント＆値を待ち受ける

    if event == sg.WIN_CLOSED:                                  #　ユーザが終了操作をしたら画面終了
        break

    if event == '計算':                                         #  ボタンクリックで計算イベントが発生したら
        縦 = float(values['-TATE-'])                            #  変数「縦」に縦の長さを代入し
        横 = float(values['-YOKO-'])                            #  変数「横」に縦の長さを代入し
        面積 = 四角形の面積(縦,横)                                #  関数を使って面積計算を実行

        window['-OUTPUT-'].update(f'四角形の面積:{面積}平方単位です。') # 計算結果を所定位置に表示

window.close()                                                  # ユーザの終了操作に連動しウィンドウを消去