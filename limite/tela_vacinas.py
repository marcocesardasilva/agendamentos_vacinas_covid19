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
            [sg.Button('Listar doses por fabricante', size=(30, 2), key='5')],
            [sg.Button('Listar doses aplicadas', size=(30, 2), key='6')],
            [sg.Button('Retornar', size=(30, 2), key='0')]
            ]
        window = sg.Window('Vacinas').Layout(layout)
        botao, valores = window.Read()
        opcao = int(botao)
        window.close()
        return opcao

    def pegar_dados_cadastrar(self):
        print("-------- CADASTRAR VACINA ----------")
        while True:
            try:
                fabricante = input("Fabricante: ")
                if len(fabricante) == 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido para fabricante!")
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                break
            except ValueError:
                print("Valor inválido! Digite um valor válido para a quantidade.")
        return {"fabricante": fabricante, "quantidade": quantidade}

    def pegar_dados_editar(self):
        print("-------- EDITAR VACINA ----------")
        while True:
            try:
                fabricante = input("Fabricante: ")
                if len(fabricante) == 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido para fabricante!")
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                break
            except ValueError:
                print("Valor inválido! Digite um valor válido para a quantidade.")
        return {"fabricante": fabricante, "quantidade": quantidade}

    def pegar_quantidade(self):
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                if quantidade < 0:
                    raise TypeError
                return quantidade
            except TypeError:
                print("Valor inválido para a quantidade. Digite um valor válido.")

    def selecionar_vacina(self):
        print("---- SELECIONAR VACINA ------")
        while True:
            try:
                fabricante = input("Fabricante: ")
                if len(fabricante) == 0:
                    raise ValueError
                return fabricante
            except ValueError:
                print("Valor inválido para fabricante!")

    def mostrar_doses_disponiveis(self, dados_vacina):
        print("----------------------------------------")
        print("Fabricante: {} | Quantidade: {}".format(dados_vacina["fabricante"],dados_vacina["quantidade"]))

    def mostrar_doses_aplicadas(self, dados_vacina):
        for fabricante,quantidade in dados_vacina.items():
            print("----------------------------------------")
            print("Fabricante: {} | Quantidade: {}" .format(fabricante, quantidade))

    def vacina_ja_cadastrada(self):
        print("Fabricante digitado já existe no sistema.")

    def vacina_cadastrada(self):
        print("Vacina cadastrada com sucesso!")

    def quantidade_insuficiente(self, quantidade):
        print("Quantidade disponível insuficiente. Seu estoque é de {} doses.".format(quantidade))

    def vacina_nao_cadastrada(self):
        print("Vacina não cadastrada.")

    def sem_aplicacoes(self):
        print("Até o momento nenhuma vacina foi aplicada.")

    def lista_vazia(self):
        print("Não existem vacinas cadastradas no sistema.")

    def doses_insuficiente(self):
        print("Quantidade de doses insuficiente para a vacina.")
