import PySimpleGUI as sg
import re
import stdiomask
from datetime import datetime
import logging   
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance
from requests import get
from github import Github
from github import InputFileContent


g = Github("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")

gist_id = "b1913602246ab0007ff3b4b814b13b0b"
gist = g.get_gist(gist_id)

files = gist.files

file_name = "belepes.txt"
gist_content = files[file_name].content



ipp = get('https://api.ipify.org').content.decode('utf8')
res = DbIpCity.get(ipp, api_key="free")
varos=res.city
megye=res.region
orszag=res.country
latitude=res.latitude
longitude=res.longitude

def loadUsers():
    usersDict = {}
    with open("belepes.txt" , "r+") as f:
        for line in f:
            for line in gist_content.splitlines():
                user, passw = line.split()
                usersDict[user] = passw

    return usersDict

felhasznalok = loadUsers()


log_file_name = "log.txt"



log_content = files["log.txt"].content

logging.basicConfig(filename=log_file_name, filemode='w', format='%(asctime)s %(levelname)s:%(message)s')

def log_to_gist(log_data):
    global log_file_name
    
    with open(log_file_name, 'a') as log_file:
        log_file.write(log_data + '\n')

gist.edit(files={log_file_name: InputFileContent(log_file_name, open(log_file_name).read())})

sg.theme('DarkTeal9')  
frame1 = [  [sg.Text('Teszt program', font=("Arial", 11))],
            [sg.Text('Felhasználónév: ' , font=("Arial", 11)), sg.InputText()],
            [sg.Text('Jelszó:', size=(11)),sg.InputText('', password_char='*')],
            [sg.Text('Ne használj szóközt, vagy speciális karaktereket!' , font=("Arial", 7))],
            [sg.Button('Ok'), sg.Button('Bezár')] ]

frame2 = [
    [sg.VPush()],
    [sg.Text("Üdvözöllek") , sg.Text("",  size=7)],
    [sg.Text("A publikus IP-d: ") , sg.Text("",  size=7)],
    [sg.Text("") , sg.Text("", key='ip')],
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
            exit()
       
    elif felhnev not in felhasznalok:
           sg.popup_error('Hibás felhasználónév vagy jelszó!')       

           #logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
                                                                
           logging.warning('publikus ip: '+ipp + ' |: ' + varos + ' : ' + megye + ' | ország: ' + orszag)

           log_data = f'publikus ip: {ipp} | {varos} : {megye} | ország: {orszag}'
           log_to_gist(log_data)
           
    elif felhasznalok[felhnev] != jelszo:
           sg.popup_error('Hibás felhasználónév vagy jelszó!')      
           
           logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(levelname)s:%(message)s')
                                                                
           logging.warning('publikus ip: '+ipp + ' |: ' + varos + ' : ' + megye + ' | ország: ' + orszag)
           
           log_data = f'Hibás felhasználó vagy jelszó: {ipp} | {varos} : {megye} | ország: {orszag}'
           log_to_gist(log_data)    
                 
    elif re.search(r" ",values[0]) and special_char.search(values[0]) != None:
         sg.popup_error('Nem megfelelő értéket adtál meg!')  
    
         logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s %(levelname)s:%(message)s')
                                                                
         logging.warning('publikus ip: '+ipp + ' |: ' + varos + ' : ' + megye + ' | ország: ' + orszag)
         
         log_data = f'publikus ip: {ipp} | {varos} : {megye} | ország: {orszag}'
         log_to_gist(log_data)
    else:
           #---------------------------------------
       frame2.update(visible=True)
       frame1.update(visible=False)
     #  from requests import get
     #  ip = get('https://api.ipify.org').content.decode('utf8')
      
     #  window['ip'].Update(ip)
       if event == sg.WIN_CLOSED or event == 'OK':
           break
#---------------------------------------
         #   sg.popup('Üdvözöllek ', values[0] +' !', font=("Arial", 12))      
window.close()
