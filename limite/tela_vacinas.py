import PySimpleGUI as sg

class TelaVacinas():

    def __init__(self, controlador_vacina):
        self.__controlador_vacina = controlador_vacina

    def tela_opcoes(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Selecione a opção desejada', size=(30, 1))],
            [sg.Button('Cadastrar vacina', size=(30, 2), key='1')],
            [sg.Button('Adicionar doses', size=(30, 2), key='2')],
            [sg.Button('Subtrair doses', size=(30, 2), key='3')],
            [sg.Button('Editar vacina', size=(30, 2), key='4')],
            [sg.Button('Remover vacina', size=(30, 2), key='5')],
            [sg.Button('Listar doses por fabricante', size=(30, 2), key='6')],
            [sg.Button('Listar doses aplicadas', size=(30, 2), key='7')],
            [sg.Button('Retornar', size=(30, 2), key='0')]
        ]
        window = sg.Window('Vacinas',size=(800, 480)).Layout(layout)
        botao, valores = window.Read()
        opcao = int(botao)
        window.close()
        return opcao

    def pegar_dados_cadastrar(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Cadastrar Vacina:')],
            [sg.Text('Fabricante',size=(15, 1)), sg.InputText()],
            [sg.Text('Quantidade',size=(15, 1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas',size=(800, 480)).Layout(layout)
        while True:
            try:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancelar':
                    window.close()
                    return None
                if len(values[0]) == 0:
                    raise ValueError
                quantidade = int(values[1])
                break
            except ValueError:
                sg.popup('Valor inválido para fabricante ou quantidade.', 'Tente novamente.')
        window.close()
        return {'fabricante': values[0].upper(), 'quantidade': quantidade}

    def selecionar_vacina(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Selecionar Vacina:')],
            [sg.Text('Fabricante',size=(15, 1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas',size=(800, 480)).Layout(layout)
        while True:
            try:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancelar':
                    window.close()
                    return None
                if len(values[0]) == 0:
                    raise ValueError
                window.close()
                return values[0].upper()
            except ValueError:
                print('Valor inválido para fabricante!')

    def pegar_dados_editar(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Editar Vacina:')],
            [sg.Text('Fabricante',size=(15, 1)), sg.InputText()],
            [sg.Text('Quantidade',size=(15, 1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas',size=(800, 480)).Layout(layout)
        while True:
            try:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancelar':
                    window.close()
                    return None
                if len(values[0]) == 0:
                    raise ValueError
                quantidade = int(values[1])
                break
            except ValueError:
                sg.popup('Valor inválido para fabricante ou quantidade.', 'Tente novamente.')
        window.close()
        return {'fabricante': values[0].upper(), 'quantidade': quantidade}

    def pegar_quantidade(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Selecionar Quantidade:')],
            [sg.Text('Quantidade',size=(15, 1)), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Vacinas',size=(800, 480)).Layout(layout)
        while True:
            try:
                event, values = window.read()
                if event == sg.WIN_CLOSED or event == 'Cancelar':
                    window.close()
                    return None
                if int(values[0]) < 0:
                    raise ValueError
                quantidade = int(values[0])
                window.close()
                return quantidade
            except ValueError:
                sg.popup('Valor inválido para a quantidade.', 'Digite um valor válido.')

    def mostrar_doses_disponiveis(self, dados_vacina):
        print('----------------------------------------')
        print('Fabricante: {} | Quantidade: {}'.format(dados_vacina['fabricante'],dados_vacina['quantidade']))

    def mostrar_doses_aplicadas(self, dados_vacina):
        for fabricante,quantidade in dados_vacina.items():
            print('----------------------------------------')
            print('Fabricante: {} | Quantidade: {}' .format(fabricante, quantidade))

    def vacina_ja_cadastrada(self):
        sg.theme('Default')
        sg.popup('A vacina digitada já existe no sistema.')

    def vacina_cadastrada(self):
        sg.theme('Default')
        sg.popup('Vacina cadastrada com sucesso!')

    def quantidade_insuficiente(self, quantidade):
        sg.theme('Default')
        sg.popup('Quantidade disponível insuficiente. Seu estoque é de {} doses.'.format(quantidade))

    def vacina_nao_cadastrada(self):
        sg.theme('Default')
        sg.popup('Vacina não cadastrada.')

    def sem_aplicacoes(self):
        sg.theme('Default')
        sg.popup('Até o momento nenhuma vacina foi aplicada.')

    def lista_vazia(self):
        sg.theme('Default')
        sg.popup('Não existem vacinas cadastradas no sistema.')

    def doses_insuficiente(self):
        sg.theme('Default')
        sg.popup('Quantidade de doses insuficiente para a vacina.')
