import PySimpleGUI as sg   #Importa a lib do PySimpleGUI usando "sg" para criar interface gráfica#
import pyshorteners        #Importa a lib do pyshorteners para encurtar as url's#
import pyperclip as pc     #importa a lib do pyperclip para copiar automaticamente as url's#

while True:                #Inicia um Loop para manter o PySimpleGUI em executação#
    layout_1 = [
        [sg.Text('Coloque aqui sua Url', size=(19, 1)),  #Criando um campo de texto #
         sg.InputText(key='url', size=(50, 1))],  #Criando um campo de inserção de texto e armazena os dados na key#
        [sg.Button('Encurtar Url')]  #Criando um botão#
    ]

    window = sg.Window('Encurtador de Url', layout_1)  #Criando uma variável que armazena o layout da interface da janela#
    event, value = window.read()  #Faz a leitura da janela e a executa#

    if event == sg.WINDOW_CLOSED:  #Condição para se caso a janela for fechada#
        window.close()  #Caso a janela seja fechada, a variável que contem o layout da janela é parada/interrompida#
        break

    if event == 'Encurtar Url':  #Condição se o botão for apertado#
        url = (value['url'])  #Se o botão for apertado, a variável 'url' irá armazenar a informação da 'key' de 'sg.InpuText'#
        window.hide()  #Irá esconder a primeira janela#

    encurtador = pyshorteners.Shortener()  #Cria um objeto com 'pyshorteners' para encurtar as url's#

    shortUrl = encurtador.tinyurl.short(url)  #Variável que armazena as Url's encurtadas#

    layout_2 = [  #Cria um novo layout para outra nova janela#
        [sg.Text(shortUrl, size=(50, 1))],#Cria um campo de InputText contendo a url encurtada para copiar e colar#
        [sg.Button('Copiar')]
    ]

    window_2 = sg.Window('Encurtador de url', layout_2)  #Variável que armazena o layout da janela#
    events2, values2 = window_2.read()  #Variável que faz a leitura do layout da janela 2

    if events2 == sg.WINDOW_CLOSED:  #Condição para se caso a janela for fechada#
        window_2.close()  #Caso a janela seja fechada, a variável que contem o layout da janela é parada/interrompida#
        break
    
    if events2 == 'Copiar':  #Condição caso o botão copiar seja apertado#
        pc.copy(shortUrl)  #Copia para area de transferência a url encurtada$
        window_2.close()  #Fecha a janela 2#
        break

