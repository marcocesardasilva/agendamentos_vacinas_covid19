from datetime import datetime as datetime
import PySimpleGUI as sg


class TelaEnfermeirosCadastro():

    def __init__(self, controlador_enfermeiros):
        self.__controlador_enfermeiros = controlador_enfermeiros

    def pegar_dados_enfermeiro(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Dados do Enfermeiro:')],
            [sg.Text('Nome',size=(15, 1)), sg.InputText()],
            [sg.Text('CPF',size=(15, 1)), sg.InputText()],
            [sg.Text('Matrícula', size=(15, 1)), sg.InputText()],
            [sg.Text('Status', size=(15,1)), sg.InputCombo(('Ativo', 'Inativo'), size=(15,1))],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Enfermeiros', layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            return None
        window.close()
        dados = {"nome": values[0], "cpf": str(values[1]), "matricula": values[2], "status": values[3]}
        return dados