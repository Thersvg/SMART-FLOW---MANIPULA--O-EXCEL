from tkinter import *
import requests
from bs4 import BeautifulSoup

url = 'https://progtechsvg.github.io/generator/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
version_app = soup.find('h2').text
versionlast_app = soup.find('h3').text


link_download_app_master = str(soup.find('h4').text)
link_download_app_adm = str(soup.find('h5').text)
link_update_aplication_master = str(soup.find('h6').text)
link_update_aplication_adm = str(soup.find('h7').text)

serial_number_update_last = str(versionlast_app)
serial_number_update_now = str(version_app) 

def download_app_master():

    url = link_download_app_master
    r = requests.get(url)
    if r.status_code == requests.codes.OK:
        with open('appmaster.zip', 'wb') as f:
            f.write(r.content)
        print('Download completo')
    else:
        r.raise_for_status()

def download_app_adm():

    url = link_download_app_adm
    r = requests.get(url)
    with open('appadm.zip', 'wb') as f:
        f.write(r.content)
    return('Download completo')

def update_aplication_master():

    url = link_update_aplication_master
    r = requests.get(url)
    with open('file.py', 'wb') as f:
        f.write(r.content)
    return('Atualizado')

def update_aplication_adm():

    url = link_update_aplication_adm
    r = requests.get(url)
    with open('file.py', 'wb') as f:
        f.write(r.content)
    return('Atualizado')

if __name__=='__main__':

    font_padrao ='Tahoma'
    cor_padrao = 'grey'
    cor_padrao_caixas = 'white'
    cor_padrao_fontes = 'White'

    manager = Tk()
    manager.title('SMART FLOW - MANAGER')
    manager.geometry('500x250')
    manager.configure(background=cor_padrao)
    photo = PhotoImage(file='icon.png')
    manager.iconphoto(False,photo)
    manager.resizable(0,0)

    name_app1 = Label(manager,text='SMART FLOW - MASTER',bg='white',fg='black')
    name_app1.place(x=40,y=50,width=220,height=40)
    name_app1.config(font=(font_padrao,12))
    
    botao_app1 = Button(manager,text='Atualizar',command=update_aplication_master,bg='white',fg='Black')
    botao_app1.place(x=270,y=50,width=90,height=40)
    botao_app1.config(font=(font_padrao,12))

    botao_app12 = Button(manager,text='Baixar',command=download_app_master,bg='white',fg='Black')
    botao_app12.place(x=370,y=50,width=90,height=40)
    botao_app12.config(font=(font_padrao,12))

    atualizacao_antiga = Label(manager,text=f'Ultima atualização {serial_number_update_last}',bg=cor_padrao,fg='white')
    atualizacao_antiga.place(x=11,y=90,width=200,height=30)
    atualizacao_antiga.config(font=(font_padrao,10))

    atualizacao_atual = Label(manager,text=f'Disponivel {serial_number_update_now}',bg=cor_padrao,fg='white')
    atualizacao_atual.place(x=300,y=90,width=120,height=30)
    atualizacao_atual.config(font=(font_padrao,10))

    name_app2 = Label(manager,text='SMART FLOW - ADM',bg='white',fg='black')
    name_app2.place(x=40,y=140,width=220,height=40)
    name_app2.config(font=(font_padrao,12))
    
    botao_app2 = Button(manager,text='Atualizar',command=update_aplication_adm,bg='white',fg='Black')
    botao_app2.place(x=270,y=140,width=90,height=40)
    botao_app2.config(font=(font_padrao,12))

    botao_app21 = Button(manager,text='Baixar',command=download_app_adm,bg='white',fg='Black')
    botao_app21.place(x=370,y=140,width=90,height=40)
    botao_app21.config(font=(font_padrao,12))

    atualizacao_antiga2 = Label(manager,text=f'Ultima atualização {serial_number_update_last}',bg=cor_padrao,fg='white')
    atualizacao_antiga2.place(x=11,y=180,width=200,height=30)
    atualizacao_antiga2.config(font=(font_padrao,10))

    atualizacao_atual2 = Label(manager,text=f'Disponivel {serial_number_update_now}',bg=cor_padrao,fg='white')
    atualizacao_atual2.place(x=300,y=180,width=120,height=30)
    atualizacao_atual2.config(font=(font_padrao,10))

    manager.mainloop()