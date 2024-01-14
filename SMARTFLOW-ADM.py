from tkinter import *
from openpyxl import Workbook
import openpyxl
import zmq
import threading
import datetime
from openpyxl.drawing.image import Image
from PIL import Image as PILImage
from openpyxl import load_workbook
from PIL import Image
from openpyxl.drawing.image import Image
import time
import requests
from bs4 import BeautifulSoup

def Atualizar_bloco():
    try:
        arquivo = open(string_caminho+f'Bloco{numero}.txt','r')
        cont = arquivo.read()
        texto_string = ''.join(cont)
        aba_texto.delete(1.0,END)
        aba_texto.insert(END,texto_string)
        nome_bloco = str(pegar_nome_bloco())
        nome_bloco_atual.config(text=nome_bloco)
    except:
        retorno_dialog.config(text=f'Não existe Bloco{numero}.txt')

def comunication_master():

    context = zmq.Context()
    rep_socket = context.socket(zmq.REQ)
    rep_socket.connect("tcp://127.0.0.1:5555")

    rep_socket.send_string('select_operation')
    request = rep_socket.recv_string()        
    return(request)

def pegar_nome_bloco():
        arquivo = open(string_caminho+f'Bloco{numero}.txt','r')
        nome_bloco = arquivo.readlines(1)
        nome_bloco_sem_nova_linha = [linha.rstrip() for linha in nome_bloco]  #REMOVE O \N DO FINAL
        nome_bloco_string = ''.join(nome_bloco_sem_nova_linha) #REMOVE ['NOME'] TRANSFORMA LISTA EM STRING
        return nome_bloco_string

def apagar_conteudo_textoaba():
    aba_texto.delete(1.0,END)
    nome_bloco_atual.config(text='')

def apagar_dialog():
        retorno_dialog.config(text='')
      
def avancar_blocos_botao():
        global numero
        numero += 1
        apagar_dialog()

        try:
                prox_bloco = open(string_caminho+f'Bloco{numero}.txt','r')
                arquivo_prox_bloco = prox_bloco.read()
                string_arquivo_prox_bloco = ''.join(arquivo_prox_bloco)
                aba_texto.delete(1.0,END)
                aba_texto.insert(END,string_arquivo_prox_bloco)
                nome_bloco = str(pegar_nome_bloco())
                nome_bloco_atual.config(text=nome_bloco)
        except:
              retorno_dialog.config(text='Não há mais blocos.')

def retroceder_blocos_botao():
        global numero
        numero = numero
        numero -= 1
        apagar_dialog()

        if numero < 0:
              numero = 0

        try:
                prox_bloco = open(string_caminho+f'Bloco{numero}.txt','r')
                arquivo_prox_bloco = prox_bloco.read()
                string_arquivo_prox_bloco = ''.join(arquivo_prox_bloco)
                aba_texto.delete(1.0,END)
                aba_texto.insert(END,string_arquivo_prox_bloco)
                nome_bloco = str(pegar_nome_bloco())
                nome_bloco_atual.config(text=nome_bloco)
        except:
              retorno_dialog.config(text='Não há mais blocos.')

def sheet_key_nuvem():     
        url = 'https://progtechsvg.github.io/generator/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragrafo = soup.find('p').text
        return(paragrafo)

def verificar_chave():
       chave_digitada = str(cont_chave.get(1.0, END+'-1c'))
       chave_sistema = str(sheet_key_nuvem())

       if chave_digitada == chave_sistema:
              chave_certa_incorreta.config(text='Chave correta!')
              arquivo_chave = open('key.txt','w')
              arquivo_chave.writelines(chave_digitada)
              arquivo_chave.close()
              chave_ativacao.destroy()
       else:
              chave_certa_incorreta.config(text='Chave incorreta')

def salvar_caminho():
       
    arquivo_caminho = open('loc.txt','w')
    location = caminho_grades.get(1.0,END+'-1c')
    arquivo_caminho.writelines(location)
    arquivo_caminho.close
    
def criar_novo_bloco():
    try:
      arquivo = open(string_caminho+f'Bloco{numero}.txt','w')
      informacao = aba_texto.get(1.0,END+'-1c')
      arquivo.write(informacao)
      arquivo.close()
      retorno_dialog.config(text='Bloco criado.')
    except:
        retorno_dialog.config(text='Algo deu errado')  

def recuperar_info_bloco():
      
    arquivo_txt = open(string_caminho+f'Bloco{numero}.txt','r')
    inf_arquivo_txt = arquivo_txt.read()
    arquivo_txt2 = open('b_up.txt','r')
    inf_arquivo_txt2 = arquivo_txt2.read()
    retorno_dialog.config(text='Copiado.')
      
    if inf_arquivo_txt2 == '':
            arquivo_txt2 = open('b_up.txt','w')
            arquivo_txt2.write(inf_arquivo_txt)
            arquivo_txt2.close()
    else:
            arquivo_txt = open(string_caminho+f'Bloco{numero}.txt','w')
            arquivo_txt.write(inf_arquivo_txt2)
            arquivo_txt.close()
            retorno_dialog.config(text='Restaurado.')
            arquivo_txt2 = open('b_up.txt', 'w') #LIMPA O ARQUIVO TXT BACKUP
            pass #LIMPA O ARQUIVO TXT BACKUP


if __name__=='__main__':

    url = 'https://progtechsvg.github.io/generator/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    status_online = soup.find('h2').text
    desenvolvedor_text = soup.find('h1').text

    caminho_salvo = open('loc.txt','r')
    caminho_loc = caminho_salvo.readlines()
    string_caminho = ''.join(caminho_loc)
    
    numero = 0
    nome_bloco = str(pegar_nome_bloco())

    font_padrao ='Tahoma'
    cor_padrao = '#2E8B57'
    cor_padrao_caixas = 'white'
    cor_padrao_fontes = 'White'
    chave_sist = str(sheet_key_nuvem())

    arquivo_txt_key = open('key.txt', 'r')
    key_verific = arquivo_txt_key.readlines()
    chave_ativ_cliente = ''.join(key_verific)

    if chave_ativ_cliente == '':

        chave_ativacao = Tk()
        chave_ativacao.title('Autenticação')
        chave_ativacao.geometry('500x250')
        chave_ativacao.configure(background=cor_padrao)
        chave_ativacao.resizable(0,0)

        insira_chave = Label(chave_ativacao,text='Insira sua chave',bg=cor_padrao,fg='white')
        insira_chave.place(x=120,y=40,width=240,height=40)
        insira_chave.config(font=(font_padrao,18))

        cont_chave = Text(chave_ativacao)
        cont_chave.place(x=120, y=80, width=240, height=40)
        cont_chave.config(font=(font_padrao,14))

        Confirmar_botao = Button(chave_ativacao,command=verificar_chave,text='Confirmar',bg='#dde',fg='Black')
        Confirmar_botao.place(x=185,y=130,width=100,height=40)
        Confirmar_botao.config(font=(font_padrao,12))

        chave_certa_incorreta = Label(chave_ativacao,text='',bg=cor_padrao,fg='white')
        chave_certa_incorreta.place(x=140,y=190,width=200,height=40)
        chave_certa_incorreta.config(font=(font_padrao,14)) 
        chave_ativacao.mainloop()

    elif chave_ativ_cliente == chave_sist:
                      
        janela = Tk()
        janela.title('SMART FLOW - ADM')
        janela.geometry('1280x720')
        janela.configure(background=cor_padrao)
        photo = PhotoImage(file='icon.png')
        janela.iconphoto(False,photo)
        janela.resizable(0,0)

        execute = True

        while(execute):                
                #t = threading.Thread(target=comunication_recebe)
                #t.start()

                caminho_grades = Text(janela)
                caminho_grades.place(x=575, y=600,width=370, height=25)
                caminho_grades.config(font=(font_padrao,12))
                caminho_grades.insert(END,string_caminho)

                botao_salvar_caminho = Button(janela,command=salvar_caminho, text='Salvar', bg='#dde', fg='Black')
                botao_salvar_caminho.place(x=955,y=600,width=100,height=25)
                botao_salvar_caminho.config(font=(font_padrao,12))

                botton_atualizar = Button(janela,command=Atualizar_bloco,text='Atualizar',bg='#dde', fg='Black')
                botton_atualizar.place(x=45, y=640, width=80, height=40)
                botton_atualizar.config(font=(font_padrao,12))

                botton_apagar = Button(janela,command=apagar_conteudo_textoaba,text='Limpar',bg='#dde', fg='Black')
                botton_apagar.place(x=130, y=640, width=80, height=40)
                botton_apagar.config(font=(font_padrao,12))

                botton_criar_novo_bloco = Button(janela,command=criar_novo_bloco,text='Criar',bg='#dde', fg='Black')
                botton_criar_novo_bloco.place(x=215, y=640, width=80, height=40)
                botton_criar_novo_bloco.config(font=(font_padrao,12))

                botton_recup_novo_bloco = Button(janela,command=recuperar_info_bloco,text='Backup',bg='#dde', fg='Black')
                botton_recup_novo_bloco.place(x=300, y=640, width=80, height=40)
                botton_recup_novo_bloco.config(font=(font_padrao,12))

                botton_adiantar = Button(janela,command=avancar_blocos_botao,text='>',bg='#dde', fg='Black')
                botton_adiantar.place(x=468, y=640, width=78, height=40)
                botton_adiantar.config(font=(font_padrao,12))

                botton_retroceder = Button(janela,command=retroceder_blocos_botao,text='<',bg='#dde', fg='Black')
                botton_retroceder.place(x=385, y=640, width=78, height=40)
                botton_retroceder.config(font=(font_padrao,12))

                '''
                botao_aplicar = Button(janela,text='Exportar',bg='#dde', fg='Black')
                botao_aplicar.place(x=1160, y=640, width=85, height=40)
                botao_aplicar.config(font=(font_padrao,12))
                '''

                botao_limpar_dialog = Button(janela,command=apagar_dialog,text='Limpar',bg='#dde', fg='Black')
                botao_limpar_dialog.place(x=1070, y=640, width=190, height=40)
                botao_limpar_dialog.config(font=(font_padrao,12))

                aba_texto = Text(janela)
                aba_texto.place(x=45, y=30, width=500,height=600)
                scrollbar = Scrollbar(janela, command=aba_texto.yview)
                scrollbar.place(x=525, y=30, width=20,height=600)
                aba_texto.config(yscrollcommand=scrollbar.set,bg=cor_padrao_caixas,font=(font_padrao,16))

                retorno_dialog = Label(janela,font=font_padrao, bg=cor_padrao_caixas, fg='Black')
                retorno_dialog.place(x=575, y=640, width=480, height=40)
                retorno_dialog.config(font=(font_padrao,14))

                online = Label(janela,text=status_online,font=font_padrao,bg=cor_padrao , fg=cor_padrao_fontes)
                online.place(x=1185, y=10, width=100, height=30)
                online.config(font=(font_padrao,12))

                desenvolvedor = Label(janela,text=desenvolvedor_text,font=font_padrao,bg=cor_padrao , fg=cor_padrao_fontes)
                desenvolvedor.place(x=1185, y=35, width=100, height=30)
                desenvolvedor.config(font=(font_padrao,10))

                bloco_atual_indicador = Label(janela,text='Bloco Atual:', font=font_padrao,bg=cor_padrao, fg=cor_padrao_fontes)
                bloco_atual_indicador.place(x=550, y=40,width=150, height=30)
                bloco_atual_indicador.config(font=(font_padrao,15))

                nome_bloco_atual = Label(janela,bg=cor_padrao, fg=cor_padrao_fontes)
                nome_bloco_atual.place(x=700, y=40,width=400, height=30)
                nome_bloco_atual.config(font=(font_padrao,14),text=nome_bloco)
                        
                Atualizar_bloco()
                janela.mainloop()
                execute = False
    else:
        arquivo_txt_key = open('key.txt', 'w')
        pass