from datetime import datetime as datetime
import PySimpleGUI as sg


class TelaEnfermeiros():

    def __init__(self, controlador_enfermeiros):
        self.__controlador_enfermeiros = controlador_enfermeiros

    def tela_opcoes(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Selecione a opção desejada', size=(30, 1))],
            [sg.Button('Cadastrar enfermeiro', size=(30, 2), key='1')],
            [sg.Button('Editar enfermeiro', size=(30, 2), key='2')],
            [sg.Button('Alterar status do enfermeiro', size=(30, 2), key='3')],
            [sg.Button('Listar enfermeiros', size=(30, 2), key='4')],
            [sg.Button('Listar pacientes atendidos por um determinado enfermeiro', size=(30, 2), key='5')],
            [sg.Button('Remover Enfermeiro', size=(30, 2), key='6')],
            [sg.Button('Retornar', size=(30, 2), key='0')]
        ]
        window = sg.Window('Enfermeiros', size=(800, 480), element_justification="center").Layout(layout).Finalize()
        window.Maximize()
        botao, valores = window.read()
        try:
            opcao = int(botao)
            window.close()
            return opcao
        except TypeError:
            pass
        window.close()

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
        window = sg.Window('Enfermeiros', layout, size=(800, 480), element_justification="center").Finalize()
        window.Maximize()
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancelar':
            window.close()
            return None
        window.close()
        dados = {"nome": values[0], "cpf": str(values[1]), "matricula": values[2], "status": values[3]}
        return dados

    def mensagem(self, mensagem=0):
        sg.theme('Default')
        sg.popup(f'{mensagem}', no_titlebar=True)

    def selecionar_enfermeiro_tabela(self, dados_enfermeiro, titulo):
        titulos = [dados_enfermeiro[0][0], dados_enfermeiro[0][1], dados_enfermeiro[0][2], dados_enfermeiro[0][3]]
        sg.theme('Default')
        layout = [[sg.Table(values=dados_enfermeiro[1:][:], headings=titulos, max_col_width=25,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='left',
                            alternating_row_color='lightgrey',
                            key='dado',
                            row_height=35,
                            tooltip='This is a table')],
                  [sg.Button('Selecionar', size=(20, 2)), sg.Button('Sair', size=(20, 2))],
                  ]
        window = sg.Window(titulo, layout,size=(800, 480), element_justification="center").Finalize()
        window.Maximize()
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Sair':
                break
            elif event == 'Selecionar':
                window.close()
                return values['dado']
        window.close()

    def mostrar_enfermeiro_tabela(self, dados_enfermeiro, titulo):
        titulos = [dados_enfermeiro[0][0], dados_enfermeiro[0][1], dados_enfermeiro[0][2], dados_enfermeiro[0][3]]
        sg.theme('Default')
        layout = [[sg.Table(values=dados_enfermeiro[1:][:], headings=titulos, max_col_width=25,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='left',
                            alternating_row_color='lightgrey',
                            key='dado',
                            row_height=35,
                            tooltip='This is a table')],

                  [sg.Button('ok')]
                  ]
        window = sg.Window(titulo, layout,size=(800, 480), element_justification="center").Finalize()
        window.Maximize()
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'ok':
                break
        window.close()
        return None

    def status_enfermeiro(self, matricula):
        sg.theme('Default')
        while True:
            try:
                status_desejado = sg.popup_yes_no(f"Deseja definir o status do enfermeiro {matricula} como Ativo?")
                print(status_desejado)
                if status_desejado == 'Yes':
                    return "Ativo"
                elif status_desejado == 'No':
                    return "Inativo"
                else:
                    sg.popup('Você digitou um valor inválido')
                    break
            except (ValueError, TypeError):
                sg.popup('Você digitou um valor inválido')
                break

    def mostrar_pacientes_por_enfermeiro(self, dados_enfermeiro, dados_paciente):
        titulos = [dados_paciente[0][0], dados_paciente[0][1], dados_paciente[0][2]]
        sg.theme('Default')
        layout = [[sg.Text(
            f'Pacientes atendidos pelo enfermeiro {dados_enfermeiro["nome"]}, matricula {dados_enfermeiro["matricula"]}:')],
                  [sg.Table(values=dados_paciente[1:][:], headings=titulos, max_col_width=25,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='left',
                            alternating_row_color='lightgrey',
                            key='dado',
                            row_height=35,
                            tooltip='This is a table')],
                  [sg.Button('Sair', size=(20, 2))],
                  ]
        window = sg.Window('Enfermeiros', layout, size=(800, 480), element_justification="center").Finalize()
        window.Maximize()
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'Sair':
                break
        window.close()

    def enfermeiro_nao_cadastrado(self):
        sg.theme('Default')
        sg.popup("Enfermeiro não cadastrado para o código digitado.", no_titlebar=True)

    def enfermeiro_inativo(self):
        sg.theme('Default')
        sg.popup("Enfermeiro selecionado inativo.", no_titlebar=True)

    def cpf_ja_cadastrado(self, cpf):
        sg.theme('Default')
        sg.popup(f'O cpf {cpf} já foi cadastrado', no_titlebar=True)

    def matricula_ja_cadastrada(self, matricula):
        sg.theme('Default')
        sg.popup(f'A matrícula {matricula} já foi cadastrada', no_titlebar=True)

    def nenhum_enfermeiro(self):
        sg.theme('Default')
        sg.popup('Ainda não há enfermeiros cadastrados', no_titlebar=True)

    def nenhum_agendamento(self):
        sg.theme('Default')
        sg.popup('Ainda não há atendimentos agendados para nenhum enfermeiro', no_titlebar=True)
