__author__ = "Alberto Neto Vilas"
__email__ = "anv7345@gmail.com"

import PySimpleGUI as sg
import PrecosWorten as pw

print(pw.call())


layout = [[sg.Text('Persistent window')],
          [sg.Button('Make Scrap'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.Read()
    if event == 'Make Scrap':
        pw.retrive_products(pw.getpages())
        print(event)
    elif event =='Exit'  or event is None:
        window.Close()
        break

sg.PopupOK('Done')
