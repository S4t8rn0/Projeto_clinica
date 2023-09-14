#Passo 1
#Importando Json
import json
agenda= list()

with open('Projeto\Cadastro_login.json', 'r', encoding= 'utf-8') as openfile:
    agenda= json.load(openfile)

#Importando o PySimpleGUI:
import PySimpleGUI as sg

#Criando as janelas:
#janela1-Login ou cadastro.
def possui():
    layout = [
        [sg.Text('O paciente possui cadastro?')],
        [sg.Button('Possui'), sg.Button('Não possui')]
    ]
    return sg.Window('Login ou cadastro', layout= layout, finalize=True)

#Janela2- Cadastro.
def cadastro():
    layout= [
        [sg.Text('Cadastro')],
        [sg.Text('Nome')],
        [sg.InputText()],
        [sg.Text('CPF')],
        [sg.InputText()],
        [sg.Text('Celular')],
        [sg.InputText()],
        [sg.Text('Endereço')],
        [sg.InputText()],
        [sg.Text('Fuma'), sg.Checkbox('Sim', key= 'Fuma'), sg.Checkbox('Não', key= 'Não fuma')],
        [sg.Text('Consumo de bebida alcóolicas'), sg.Checkbox('Sim', key= 'Bebida'), sg.Checkbox('Não', key= 'Não bebe')],
        [sg.Text('Algum procedimento recente'), sg.Checkbox('Sim', key='Procedimento'), sg.Checkbox('Não', key= 'Procedimento')],
        [sg.Button('Confirmar'), sg.Button('Cancel')]
    ]
    return sg.Window('Cadastro', layout= layout, finalize=True)

#Janela3- Caso o paciente possua login.
def login():
    layout=[
        [sg.Text('Login')],
        [sg.Text('Nome')],
        [sg.InputText()],
        [sg.Text('CPF')],
        [sg.InputText()],
        [sg.Button('Confirmar'), sg.Button('Cancel')]
    ]
    return sg.Window('Login', layout= layout, finalize=True)

janela1, janela2, janela3 = possui(), None, None

while True:
    window, event, values= sg.read_all_windows()
    #JANELA1: O paciente já possui cadastro.
    if window== janela1 and event== 'Possui':
        janela1.hide()
        janela3= login()
    
    #JANELA1: Paciente não possui cadastro.
    if window== janela1 and event== 'Não possui':
        janela1.hide()
        janela2= cadastro
    
    #JANELA1: Windows close.
    if window== janela1 and event== sg.WINDOW_CLOSED:
        sg.popup_yes_no('Tem certeza que deseja fechar?')
        if event in ('Sim'):
            print('Ok')
            break
        if event in('não'):
            janela1()

    #JANELA2: Cadastrando.
    if window== janela2 and event == 'Confirmar':
        janela2.hide()
        agenda.append(dict( Nome= values[0], CPF= values[1], Celular= values[2], Endereço= values[3], Fuma= ['Fuma'], Bebida= ['Bebida'], Procedimento= ['Procedimento']))
        with open('Projeto\Cadastro_login.json', 'a', encoding= 'utf-8') as openfile:
            json.dump(agenda, openfile, ensure_ascii= False, indent= '\t')
        print(agenda)
        break
    
    #JANELA2: Caso tenha clicado em não(janela1) sem querer.
    if window== janela2 and event== 'Cancel':
        janela2.hide()
        janela1.un_hide()
    
    #JANELA2: Windows close.
        if window== janela2 and event== sg.WINDOW_CLOSED:
            sg.popup_yes_no('Tem certeza que deseja fechar?')
            if event in ('Sim'):
                print('Ok')
                break
            if event in('não'):
                janela2()


    #JANELA3: Puxando as informações do paciente que já possui cadastro.
    if window== janela3 and event== 'Confirmar':
        janela3.hide()
        sg.popup('Informações corretas.')
        agenda.append(dict( Nome= values[0], CPF= values[1]))
        with open('Projeto\Cadastro_login.json', 'a', encoding= 'utf-8') as openfile:
            json.dump(agenda, openfile, ensure_ascii= False, indent= '\t')
        print(agenda)
        break

    #JANELA3: Caso tenha clicado em confirmar(janela1) sem querer.
    if window== janela3 and event== 'Cancel':
        janela3.hide()
        janela1.un_hide()

    #JANELA3: Windows close.
    if window== janela3 and event== sg.WINDOW_CLOSED:
        sg.popup_yes_no('Tem certeza que deseja fechar?')
        if event in ('Sim'):
            print('Ok')
            break
        if event in('não'):
            janela3()
