import json

pacot= list()

with open('Projeto\Pacote.json', 'r', encoding= 'utf-8') as openfile:
    pacot= json.load(openfile)

import PySimpleGUI as sg

def desejo():
    layout= [
        [sg.Text('Pacotes')],
        [sg.Text('Deseja olhar os pacotes de procedimento?')],
        [sg.Button('Sim'), sg.Button('Não')]
        ]
    return sg.Window('Pacote', layout= layout, finalize= True)
    return 'Nome'

def pacote():
    layout= [
        [sg.Text('Pacotes')],
        [sg.Text('Nome'), sg.InputText(k='nome')],
        [sg.Text('Temos os seguintes tamanhos dos pacotes:')],
        [sg.Text('P- 3 sessões/aplicações')], 
        [sg.Text('M- 6 sessões/aplicações')],
        [sg.Text('G- 9 sessões/aplicações')],
        [sg.Checkbox('P', key= 'Pequeno'), sg.Checkbox('M', key= 'Medio'), sg.Checkbox('G', key= 'Grande')],
        [sg.Button('Confirmar'), sg.Button('Cancel')]
        ]
    return sg.Window('Pacotes', layout= layout, finalize= True)
    
janela6, janela7 = desejo(), None

while True:
    window, event, values= sg.read_all_windows()

    #JANELA6: Deseja olhar os pacotes.
    if window == janela6 and event == 'Sim':
        janela6.hide()
        janela7= pacote()
        
    #JANELA6: Não deseja olhar os pacotes.
    if window == janela6 and event == 'Não':
        break
    
    #JANELA6: Windows close.
    if window== janela6 and event== sg.WINDOW_CLOSED:
        sg.popup_yes_no('Tem certeza que deseja fechar?')
        if event == 'Sim':
            print('Ok')
            break
        if event == 'Não':
            pacote()


    #JANELA7:
    if window== janela7 and event == 'Confirmar':
        if values['Pequeno'] == True and values['Medio'] == False and values['Grande'] == False:       
            pacot.append(dict(Pacote= values['Pequeno'] and 'Pequeno', Paciente= values[0]))

            with open('Projeto\Pacote.json', 'w', encoding= 'utf-8') as openfile:
                json.dump(pacot, openfile, ensure_ascii= False, indent= '\t')

            sg.popup ('Seu pacote Pequeno com 3 sessões foi selecionado. Agora é só aproveita-ló.')    
            break
        
        elif values['Medio'] == True and values['Pequeno'] == False and values['Grande'] == False:
            pacot.append(dict(Pacote= values['Medio'] and 'Médio', Paciente= values[0]))

            with open('Projeto\Pacote.json', 'w', encoding= 'utf-8') as openfile:
                json.dump(pacot, openfile, ensure_ascii= False, indent= '\t')

            sg.popup ('Seu pacote Médio com 6 sessões foi selecionado. Agora é só aproveita-ló.')
            break
        
        elif values['Grande']== True and values['Medio'] == False and values['Pequeno'] == False:
            
            pacot.append(dict(Pacote= values['Grande'] and 'Grande', Paciente= values[0]))

            with open('Projeto\Pacote.json', 'w', encoding= 'utf-8') as openfile:
                json.dump(pacot, openfile, ensure_ascii= False, indent= '\t')
            
            sg.popup ('Seu pacote Grande com 10 sessões, uma saindo de graça, foi selecionado. Agora é só aproveita-ló.')
            break
        
    #JANELA7:
    if window == janela7 and event == 'Cancel':
        janela7.hide()
        janela6.un_hide() 
    
    #JANELA7: Windows close.
    if window== janela7 and event== sg.WINDOW_CLOSED:
        sg.popup_yes_no('Tem certeza que deseja fechar?')
        if event in ('Sim'):
            print('Ok')
            break
        if event in('não'):
            janela7()
        

        


