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
           #[sg.Button('Consultar enfermeiro', size=(30, 2), key='3')],
            [sg.Button('Alterar status do enfermeiro', size=(30, 2), key='4')],
            [sg.Button('Listar enfermeiros', size=(30, 2), key='5')],
            [sg.Button('Listar pacientes atendidos por um determinado enfermeiro', size=(30, 2), key='6')],
            [sg.Button('Retornar', size=(30, 2), key='0')]
            ]
        window = sg.Window('Enfermeiros',size=(800, 480)).Layout(layout)
        botao, valores = window.read()
        try:
            opcao = int(botao)
            return opcao
        except TypeError:
            pass
        window.close()

    def mensagem(self, mensagem=0):
        sg.theme('Default')
        sg.popup(f'{mensagem}')

    def get_enfermeiro_matricula(self):
        return sg.popup_get_text('Digite a Matríula do enfermeiro: ')


    def pegar_dados_enfermeiro(self):
        print("-------- INCLUIR ENFERMEIRO ----------")
        while True:
            try:
                nome = input("Nome: ").upper()
                if nome.replace(' ', '').isalpha():
                    break
                else:
                    print(f'O nome {nome} é inválido!')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        while True:
            try:
                cpf = input("CPF (apenas números): ").replace(' ', '')
                if cpf.isnumeric() and len(cpf) == 11:
                    break
                else:
                    print(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        while True:
            try:
                matricula = input("Matrícula (4 dígitos): ").replace(' ','')
                if matricula.isnumeric() and len(matricula) == 4:
                    break
                else:
                    print(f'A matrícula {matricula} é inválida!\nDigite uma matrícula com 4 dígitos')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')

        return {"nome": nome, "cpf": cpf, "matricula": matricula, "status": "Ativo"}

    def pegar_dados_enfermeiro_edicao(self):
        print("-------- EDITAR ENFERMEIRO ----------")
        while True:
            try:
                nome = input("Nome: ").upper()
                if nome.replace(' ', '').isalpha():
                    break
                else:
                    print(f'O nome {nome} é inválido!')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        while True:
            try:
                matricula = input("Matrícula (4 dígitos): ").replace(' ','')
                if len(matricula) == 4 and matricula.isnumeric():
                    break
                else:
                    print(f'A matrícula {matricula} é inválida!\nDigite uma matrícula com 4 dígitos')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        return {'nome': nome, 'matricula': matricula}

    def selecionar_enfermeiro(self):
        print('----- SELECIONAR ENFERMEIRO -----')
        while True:
            try:
                matricula = input("Matrícula (4 dígitos): ").replace(' ','')
                if matricula.isnumeric() and len(matricula) == 4:
                    break
                else:
                    print(f'A matrícula {matricula} é inválida!\nDigite uma matrícula com 4 dígitos')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        return matricula


    def mostrar_enfermeiro(self, dados_enfermeiro):
        self.linha()
        print(f'ENFERMEIRO: {dados_enfermeiro["nome"]} |'
              f' CPF: {dados_enfermeiro["cpf"]} |'
              f' MATRÍCULA: {dados_enfermeiro["matricula"]} |'
              f' STATUS: {dados_enfermeiro["status"]}'
              )
        self.linha()

    def mostrar_enfermeiro_tabela(self, dados_enfermeiro):
        titulos = [dados_enfermeiro[0][0], dados_enfermeiro[0][1], dados_enfermeiro[0][2], dados_enfermeiro[0][3]]
        sg.theme('Default')
        layout = [[sg.Table(values=dados_enfermeiro[1:][:], headings=titulos, max_col_width=25,
                             # background_color='light blue',
                             auto_size_columns=True,
                             display_row_numbers=True,
                             justification='right',
                             alternating_row_color='lightgrey',
                             key='dado',
                             row_height=35,
                             tooltip='This is a table')],
                  [sg.Button('Selecionar', size=(20, 2)), sg.Button('Sair', size=(20, 2))],
                  ]
        window = sg.Window('The Table Element', layout,
                           #botao, valores = window.Read()
                           )
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

    def status_enfermeiro(self, matricula):
        sg.theme('Default')
        while True:
            try:
                status_desejado = sg.popup_get_text(f"Alterar status do enfermeiro {matricula}: \nPara definir status como <Ativo> digite 1,\nPara definir status como <Inativo> digite 2")
                if status_desejado == 1:
                    return "Ativo"
                elif status_desejado == 2:
                    return "Inativo"
                else:
                    print('Você digitou um valor inválido')
            except (ValueError, TypeError):
                print('Você digitou um valor inválido')

    def mostrar_lista_enferemrios(self, dados_enfermeiro):
        print(
            f'NOME: {dados_enfermeiro["nome"]} |'
            f' CPF: {dados_enfermeiro["cpf"]} |'
            f' MATRÍCULA: {dados_enfermeiro["data_nascimento"]}')

    def mostrar_pacientes_por_enfermeiro(self, dados_paciente):
        idade_dias = datetime.today().date() - dados_paciente["data_nascimento"]
        idade = idade_dias.days // 365.24231481481481481481481481481481
        print(f'PACIENTE: {dados_paciente["nome"]} |'
              f' CPF: {dados_paciente["cpf"]} |'
              f' Idade: {idade:.0f} anos')

    def linha(self):
        print("-" * 70)

    def enfermeiro_nao_cadastrado(self):
        print("Enfermeiro não cadastrado para o código digitado.")
    
    def enfermeiro_inativo(self):
        print("Enfermeiro selecionado inativo.")

    def cpf_ja_cadastrado(self, cpf):
        print(f'O cpf {cpf} já foi cadastrado')

    def matricula_ja_cadastrada(self, matricula):
        print(f'A matrícula {matricula} já foi cadastrada')

    def nenhum_enfermeiro(self):
        print('Ainda não há enfermeiros cadastrados')

    def nenhum_agendamento(self):
        print('Ainda não há atendimentos agendados para nenhum enfermeiro')