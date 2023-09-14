#Passo 2
import json
anamnese= list()

with open('Projeto/Anamnese.json', 'r', encoding= 'utf-8') as openfile:
    anamnese= json.load(openfile)

import PySimpleGUI as sg

#JANELA1: Pré-consulta.
def anamn():
    layout = [
        [sg.Text('Anamnese')],
        [sg.Text('Qual o procedimento desejado?')],
        [sg.InputText()],
        [sg.Text('Alergia:')],
        [sg.InputText()],
        [sg.Text('Problema de pele:')],
        [sg.InputText()],
        [sg.Text('Realizando algum tratamento?')],
        [sg.Checkbox('Sim', key= 'Tratamento'), sg.Checkbox('Não', key= 'Nenhum')],
        [sg.Text('Fez cirurgia recentemente?')],
        [sg.Checkbox('Sim', key= 'Cirurgia'), sg.Checkbox('Não', key= 'N')],
        [sg.Text('Gestante?')],
        [sg.Checkbox('Sim', key= 'Bebê'), sg.Checkbox('Não', key= 'Nop')],
        [sg.Button('Confirmar'), sg.Button('Cancel')]
        ]
    return sg.Window('Anamnese', layout= layout, finalize= True)

janela1 = anamn() 

while True:
    window, event, values= sg.read_all_windows()
    if window == janela1 and event== 'Confirmar':
        anamnese= dict(Desejo= values[0], Alergia= values[1], Gestante= values['Bebê'] or values['Nop'], Problema_de_Pele= values[2], Tratamento= values['Tratamento'] or values['Nenhum'], Cirurgia= values['Cirurgia'] or values['N'])
        with open('Projeto/Anamnese.json', 'a', encoding= 'utf-8') as openfile:
         json.dump(anamnese, openfile, ensure_ascii= False, indent= '\t')
        sg.popup('Informações atualizadas.')
        break

        

    