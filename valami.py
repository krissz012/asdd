import PySimpleGUI as sg
import re
sg.theme('DarkTeal9')  
layout = [  [sg.Text('Szevasz!', font=("Arial", 11))],
            [sg.Text('Add meg a neved: ' , font=("Arial", 11)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Bezár')] ]

window = sg.Window('Proba1', layout,size=(350, 350))

while True:
    event, values = window.read()
  
        
    if event == sg.WIN_CLOSED or event == 'Bezár':
           break
       
    elif "Jázmin" in (values[0]):
           sg.popup_error('Belépés elutasítva.(reason:cigány)')
           
              
    elif re.search(r"[0-9]+",values[0]):
           sg.popup_error('Nem megfelelő értéket adtál meg!')
           
            
    else:
            sg.popup('Szevasz ', values[0] +' !', font=("Arial", 12))
    
   

window.close()
