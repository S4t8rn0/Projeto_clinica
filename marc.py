#Importando Json
import json
marc= list()
with open('Projeto\marc.json', 'r', encoding= 'utf-8') as openfile:
    marc= json.load(openfile)

#Importando a biblioteca em python que trabalha com data e hora:
import datetime as dt

#Importando o PySimpleGUI:
import PySimpleGUI as sg
#Criando as duas janelas:
'''Janela Principal'''
def janel():
    layout = [
        [sg.Text ('O paciente deseja agendar a próxima consulta?')],
        [sg.Button('Sim'), sg.Button('Não')]
    ]
    return sg.Window('Consulta', layout= layout, finalize=True)

'''Janela do agendamento'''
def janela():
    layout = [
            [sg.Text ('O paciente deseja agendar a próxima consulta?')],
            [sg.Text ('Nome do paciente: ')],
            [sg.InputText() ],
            [sg.Text('Qual dia?')],
            [sg.InputText()],
            [sg.Text('Horário:')],
            [sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    return sg.Window('Agendamento', layout= layout, finalize=True)

janela1, janela2 = janel(), None

while True:
    window, event, values= sg.read_all_windows()

    #Caso deseje fechar na primeira janela. Não deseja marcar a consulta:
    if window == janela1 and event == sg.WIN_CLOSED or event == 'Não':
        break

    #Caso deseje abrir a segunda janela. Indo marcar a consulta:
    if window == janela1 and event== 'Sim':
        janela1.hide()
        janela2= janela()

    #Caso deseje voltar para a primeira janela.
    if window== janela2 and event== 'Cancel':
        janela2.hide()
        janela1.un_hide()

    #Caso deseje marcar a consulta.
    if window == janela2 and event== 'Ok':
        #incluindo a hora e data do momento em que for acinado o botão:
        hora= dt.datetime.now() 
        #Salvando as informações em JSON:
        marc.aapend(dict(Informação= hora.strftime('%d/%m/%Y - %H:%M'), Nome= values[0], Data= values[1], Horário= values[2]))
        print(marc)
        sg.popup(f'Sua consulta foi agendada no dia {hora.day}/{hora.month}/{hora.year} às {hora.hour} : {hora.minute}.')
        with open('Projeto\marc.json', 'w', encoding= 'utf-8') as openfile:
            json.dump(marc, openfile, ensure_ascii= False, indent= '\t')
        break
