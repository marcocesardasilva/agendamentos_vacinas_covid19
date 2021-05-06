from datetime import datetime as datetime
import PySimpleGUI as sg


class TelaEnfermeirosCadastro():

    def __init__(self, controlador_enfermeiros):
        self.__controlador_enfermeiros = controlador_enfermeiros

    def pegar_dados_enfermeiro(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Cadastro de Enfermeiro:')],
            [sg.Text('Nome',size=(15, 1)), sg.InputText()],
            [sg.Text('CPF',size=(15, 1)), sg.InputText()],
            [sg.Text('Matrícula', size=(15, 1)), sg.InputText()],
            [sg.Text('Status', size=(15,1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas', layout)
        event, values = window.read()
        window.close()
        return {"nome": values[0], "cpf": values[1], "matricula": int(values[2]), "status": values[3]}