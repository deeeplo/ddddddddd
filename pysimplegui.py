import PySimpleGUI as sg 
import random
msg= ""
#pre requisites - PySimpleGUI

x = random.randint(1,20)
y = random.randint(1,20)
opval = random.randint(0,2)
if opval == 0:
    ans = x*y
elif opval == 1:
    ans = x+y
elif opval == 2:
    ans = x-y
x=str(x)
y=str(y)
operators = ["*","+","-"]
#theme for layout
sg.theme('DarkBlue2')
# no division bc decimals cant work
question = 'What is'+" "+x+" "+operators[opval]+" "+y+" "+'?'
layout = [
    [sg.Text(question,key='-OUTPUT-'), sg.InputText(do_not_clear = False)],
    [sg.Button("Submit",bind_return_key=True),sg.Text(msg,key = '-CORRECT-')],
]
window = sg.Window("Math Quiz",layout)

#create render loop
while True:
    event, values = window.read(timeout=10000)
    #closes if ok button is clicked or if window is x'ed out
    if event == sg.WIN_CLOSED:
        break
    try:
        if event == "Submit" and int(values[0]) != ans:
            msg = "Incorrect, try again"
            #print("False the answer was", ans)
            window['-CORRECT-'].update(msg,text_color='Red')
        elif event == "Submit":
            #generates new random equation
            msg = "Correct!"
            x = random.randint(1,20)
            y = random.randint(1,20)
            opval = random.randint(0,2)
            if opval == 0:
                ans = x*y
            elif opval == 1:
                ans = x+y
            elif opval == 2:
                ans = x-y
            x=str(x)
            y=str(y)
            question = 'What is'+" "+x+" "+operators[opval]+" "+y+" "+'?'
            #updes correcion message and question
            window['-CORRECT-'].update(msg,text_color='Green')
            window['-OUTPUT-'].update(question)
            #print(ans, "is correct")
    except ValueError:
        msg = "Please input a valid number"
        window['-CORRECT-'].update(msg,text_color = 'Red')

window.close()