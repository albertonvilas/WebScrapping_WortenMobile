__author__ = "Alberto Neto Vilas"
__email__ = "anv7345@gmail.com"

import PySimpleGUI as sg
import PrecosWorten as pw



layout = [
            [sg.Text('Progresso')],
            [sg.Output(size=(None, None))],
            [sg.Button('Make Scrap'), sg.Exit()]
        ]

window = sg.Window('GET INFO WORTEN', layout)

while True:
    event, values = window.Read()
    if event == 'Make Scrap':
        print("O scrap começou a ser realizado...")
        window.Refresh()
        pw.testeprogress()
        print(event)
    elif event =='Exit'  or event is None:
        window.Close()
        break
