import PySimpleGUI as sg

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ':￥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

menu_layout = [
    [sg.Checkbox(item.info(), key=f"-MENU-{i}-", enable_events=True)] for i, item in enumerate(menu_items)
]

layout = [
    [sg.Text("メニューを選択してください:")],
    *menu_layout,
    [sg.Text("個数を入力してください:"), sg.InputText(key="-COUNT-", size=(5, 1)), sg.Button("計算"), sg.Button("リセット")],
    [sg.Text("小計は 0 円です", key="-SUBTOTAL-")],
    [sg.Text("注文履歴:", size=(10, 5)), sg.Listbox(values=[], key="-HISTORY-", size=(40, 5))],
    [sg.Text("合計は 0 円です", font=('Arial',20),key="-TOTAL-")]
]

window = sg.Window("メニュー注文", layout)

order_history = []
total_price = 0

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event.startswith("-MENU-"):
        subtotal = 0
        for i, item in enumerate(menu_items):
            if values[f"-MENU-{i}-"]:
                try:
                    count = int(values["-COUNT-"])
                    subtotal += item.get_total_price(count)
                except ValueError:
                    pass

        window["-SUBTOTAL-"].update("小計は " + str(subtotal) + " 円です")

    if event == "計算":
        subtotal = 0  # 注文ごとの小計を追加
        for i, item in enumerate(menu_items):
            if values[f"-MENU-{i}-"]:
                try:
                    count = int(values["-COUNT-"])
                    subtotal += item.get_total_price(count)
                    total_price += item.get_total_price(count)
                    order_history.append(f"{item.name} × {count} = {item.get_total_price(count)} 円")
                    window[f"-MENU-{i}-"].update(False)
                    window["-COUNT-"].update("")
                except ValueError:
                    pass

        window["-SUBTOTAL-"].update("小計は " + str(subtotal) + " 円です")  # 小計を更新
        window["-TOTAL-"].update("合計は " + str(total_price) + " 円です")
        window["-HISTORY-"].update(order_history)

    if event == "リセット":
        total_price = 0
        order_history = []
        for i in range(len(menu_items)):
            window[f"-MENU-{i}-"].update(False)
        window["-COUNT-"].update("")
        window["-SUBTOTAL-"].update("小計は 0 円です")
        window["-TOTAL-"].update("合計は 0 円です")
        window["-HISTORY-"].update([])

window.close()
