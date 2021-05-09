from datetime import datetime as datetime
import PySimpleGUI as sg


class TelaPacientesCadastro():

    def __init__(self, controlador_pacientes):
        self.__controlador_pacientes = controlador_pacientes

    def pegar_dados_cadastrar(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Dados do Paciente:')],
            [sg.Text('Nome: ',size=(15, 1)), sg.InputText()],
            [sg.Text('CPF: ',size=(15, 1)), sg.InputText()],
            [sg.Text('Data de Nascimento (dd/mm/aaaa):', size=(15, 1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas', layout)
        event, values = window.Read()
        if event == 'Cancelar':
            return None
        window.close()
        return {"nome": values[0], "cpf": values[1], "data_nascimento": values[2]}