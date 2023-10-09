import PySimpleGUI as sg
import re
import stdiomask

def loadUsers():
    usersDict = {}
    with open("belepes.txt" , "r+") as f:
        for line in f:
            user, passw = line.split()
            usersDict[user] = passw
    return usersDict

felhasznalok = loadUsers()
#felhnev = input("Username")
#jelszo = input("Password") 


sg.theme('DarkTeal9')  
frame1 = [  [sg.Text('Teszt program', font=("Arial", 11))],
            [sg.Text('Felhasználónév: ' , font=("Arial", 11)), sg.InputText()],
            [sg.Text('Jelszó:', size=(11)),sg.InputText('', password_char='*')],
            [sg.Text('Ne használj szóközt, vagy speciális karaktereket!' , font=("Arial", 7))],
            [sg.Button('Ok'), sg.Button('Bezár')] ]



frame2 = [
    [sg.VPush()],
    [sg.Text("Üdvözöllek"), sg.Text("",  size=7)],
    [sg.Button("OK")],
    [sg.VPush()],
]

layout = [
    [sg.Frame("", frame1, size=(360, 200), visible=True,  key='Frame1',  element_justification='center'),
     sg.Frame("", frame2, size=(360, 200), visible=False, key='Frame2',  element_justification='center')],
]


window = sg.Window('Proba1', layout,size=(350, 180))


while True:
    frame1, frame2 = window['Frame1'], window['Frame2']
    event, values = window.read()
    
    felhnev = values[0]
    
    jelszo = values[1]
    
    special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
        
    if event == sg.WIN_CLOSED or event == 'Bezár':
           break
       
       
           

           
    elif felhnev not in felhasznalok:
           sg.popup_error('Hibás felhasználónév vagy jelszó!')       
           
    elif felhasznalok[felhnev] != jelszo:
           sg.popup_error('Hibás felhasználónév vagy jelszó!')       
                    
    elif re.search(r" ",values[0]) and special_char.search(values[0]) != None and special_char.search(values[1] != None):
         sg.popup_error('Nem megfelelő értéket adtál meg!')  
    
                   
    else:
           
           
           #---------------------------------------
       frame2.update(visible=True)
       frame1.update(visible=False)
       
       if event == sg.WIN_CLOSED or event == 'OK':
           break
       


#---------------------------------------

         #   sg.popup('Üdvözöllek ', values[0] +' !', font=("Arial", 12))
       

window.close()
