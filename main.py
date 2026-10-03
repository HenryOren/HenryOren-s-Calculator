import PySimpleGUI as sg

sg.theme("DarkGreen1")

layout = [
    [sg.Text("", key="result")],
    [sg.Button('C', key="clear"),
     sg.Button('=', key="equal")],
    [sg.Button('7', key="seven"),
     sg.Button('8', key="eight"),
     sg.Button('9', key="nine"),
     sg.Button('/', key="div")],
    [sg.Button('4', key="four"),
     sg.Button('5', key="five"),
     sg.Button('6', key="six"),
     sg.Button('*', key="mul")],
    [sg.Button('1', key="one"),
     sg.Button('2', key="two"),
     sg.Button('3', key="three"),
     sg.Button('-', key="sub")],
    [sg.Button('.', key="dot"),
     sg.Button('0', key="zero"),
     sg.Button('$', key="dollar"),
     sg.Button('+', key="add")],
]
win = sg.Window('计算器', layout)

def add_to_result(key):
    key1 = ''
    match key:
        case "zero": key1 = '0'
        case "one": key1 = '1'
        case "two": key1 = '2'
        case "three": key1 = '3'
        case "four": key1 = '4'
        case "five": key1 = '5'
        case "six": key1 = '6'
        case "seven": key1 = '7'
        case "eight": key1 = '8'
        case "nine": key1 = '9'
        case "add": key1 = '+'
        case "sub": key1 = '-'
        case "mul": key1 = '*'
        case "div": key1 = '/'
        case "dot": key1 = '.'
        case "dollar": key1 = '6.68'
    current_text = win['result'].get()
    win['result'].update(current_text + key1)

def calc():
    try:
        expression = win['result'].get()
        win['result'].update(str(eval(expression)))
    except:
        win['result'].update("ERR")

while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "clear":
        win['result'].update("")
    elif event == "equal":
        calc()
    else:
        add_to_result(event)

win.close()
