from datetime import datetime as datetime
import PySimpleGUI as sg


class TelaPacientesCadastro():

    def __init__(self, controlador_pacientes):
        self.__controlador_pacientes = controlador_pacientes

    def pegar_dados_cadastrar(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Cadastro de Paciente:')],
            [sg.Text('Nome',size=(15, 1)), sg.InputText()],
            [sg.Text('CPF',size=(15, 1)), sg.InputText()],
            [sg.Text('Data de Nascimento', size=(15, 1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas', layout)
        event, values = window.read()
        window.close()
        return {"fabricante": values[0], "quantidade": int(values[1])}