import PySimpleGUI as sg

class TelaSistema:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        sg.theme('Default')
        sg.Popup('Seja bem vindo ao sistema de agendamento de vacinações.')
        layout = [
            [sg.Text('Selecione a opção desejada', size=(30, 1))],
            [sg.Button('Enfermeiros', size=(30, 2), key='1')],
            [sg.Button('Pacientes', size=(30, 2), key='2')],
            [sg.Button('Vacinas', size=(30, 2), key='3')],
            [sg.Button('Agendamentos', size=(30, 2), key='4')],
            [sg.Button('Encerrar Sistema', size=(30, 2), key='0')]
            ]
        window = sg.Window('Sistema de agendamento de vacinações',
            grab_anywhere=False,
            size=(800, 480),
            return_keyboard_events=True,
            keep_on_top=True).Layout(layout)
        botao, valores = window.Read()
        opcao = int(botao)
        window.close()
        return opcao
