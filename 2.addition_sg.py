
import PySimpleGUI as sg

#1.レイアウトの定義と作成

layout = [[sg.Text("1つ目の数字を入力してください"), sg.InputText(key='-INPUT1-', size=(5, 1))],
           [sg.Text("2つ目の数字を入力してください"), sg.InputText(key='-INPUT2-', size=(5, 1))],
           [sg.Button("計算"), sg.Button("リセット")],
           [sg.Text('入力した２つの数字の合計は ',key='TEXT'), sg.Text(key='-OUTPUT-')]
]

#2.ウィンドウオブジェクトの生成

window = sg.Window('順次構造',layout,grab_anywhere=True)

#3.ウィンドウの表示

while True:
    event,values = window.read() #window.read()で呼んできたeventとvalueを変数event,valueに代入

#3.ウィンドウを閉じる

    if event == sg.WIN_CLOSED: 
        break 
          
    if event == '計算':
        try:
            num1 = int(values['-INPUT1-'])
            num2 = int(values['-INPUT2-'])
            result = num1 + num2
            window['-OUTPUT-'].update(f"{result}です。")
        except ValueError:
            sg.popup_error('無効な入力です。数値を入力してください。')

    if event == 'リセット':
        window['-INPUT1-'].update('')
        window['-INPUT2-'].update('')
        window['-OUTPUT-'].update('')

#windowをクローズし終了

window.close() 

