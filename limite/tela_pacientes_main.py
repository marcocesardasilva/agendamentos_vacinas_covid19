from datetime import datetime as datetime
import PySimpleGUI as sg


class TelaPacientes():

    def __init__(self, controlador_pacientes):
        self.__controlador_pacientes = controlador_pacientes

    def tela_opcoes(self):
        sg.theme('Default')
        layout = [#[sg.Table(values=lista[1:][:], max_col_width=25,
        #                     # background_color='light blue',
        #                     auto_size_columns=True,
        #                     display_row_numbers=True,
        #                     justification='right',
        #                     alternating_row_color='lightgrey',
        #                     key='-TABLE-',
        #                     row_height=35,
        #                     tooltip='This is a table')],
            [sg.Text('Selecione a opção desejada', size=(30, 1))],
            [sg.Button('Cadastrar paciente', size=(30, 2), key='1')],
            [sg.Button('Editar paciente', size=(30, 2), key='2')],
            [sg.Button('Listar pacientes cadastrados', size=(30, 2), key='3')],
            [sg.Button('Listar pacientes nunca agendados', size=(30, 2), key='4')],
            [sg.Button('Listar pacientes vacinados 1ª dose', size=(30, 2), key='5')],
            [sg.Button('Listar pacientes vacinados 2ª dose', size=(30, 2), key='6')],
            [sg.Button('Remover paciente', size=(30, 2), key='7')],
            [sg.Button('Retornar', size=(30, 2), key='0')]
            ]
        window = sg.Window('Pacientes',size=(800, 480)).Layout(layout)
        botao, valores = window.read()
        try:
            opcao = int(botao)
            window.close()
            return opcao
        except TypeError:
            pass
        window.close()

    def mensagem(self, mensagem=0):
        sg.theme('Default')
        sg.popup(f'{mensagem}', no_titlebar=True)

    # def pega_dados_paciente(self):
    #     print("-------- INCLUIR PACIENTE ----------")
    #     while True:
    #         try:
    #             nome = input("Nome: ").upper()
    #             if nome.replace(' ','').isalpha():
    #                 break
    #             else:
    #                 print(f'O nome {nome} é inválido!')
    #         except (ValueError, TypeError):
    #             print('Houve problemas com o tipo de dado digitado')
    #     while True:
    #         try:
    #             cpf = input("CPF (apenas números): ").replace(' ','')
    #             if cpf.isnumeric() and len(cpf) == 11:
    #                 break
    #             else:
    #                 print(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
    #         except (ValueError, TypeError):
    #             print('Houve problemas com o tipo de dado digitado')
    #     while True:
    #         try:
    #             data_nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")
    #             data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
    #             idade_dias = datetime.today().date() - data_nascimento_obj
    #             idade = int(idade_dias.days // 365.24231481481481481481481481481481)
    #             if 0 < idade < 150:
    #                 break
    #             else:
    #                 print('Idade inválida, a idade deve ser entre 0 e 150 anos')
    #
    #         except:
    #             print('Data inválida, a data deve ser inserida neste formato: 11/11/2011')
    #     return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento_obj}
    #
    # def pega_dados_paciente_edicao(self):
    #     print('---------- EDITAR PACIENTE ----------')
    #     while True:
    #         try:
    #             nome = input("Nome: ").upper()
    #             if nome.replace(' ','').isalpha():
    #                 break
    #             else:
    #                 print(f'O nome {nome} é inválido!')
    #         except (ValueError, TypeError):
    #             print('Houve problemas com o tipo de dado digitado')
    #     while True:
    #         try:
    #             data_nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")
    #             data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
    #             idade_dias = datetime.today().date() - data_nascimento_obj
    #             idade = int(idade_dias.days // 365.24231481481481481481481481481481)
    #             if 0 <= idade <= 150:
    #                 break
    #             else:
    #                 print('Idade inválida, a idade deve ser entre 0 e 150 anos')
    #
    #         except:
    #             print('Data inválida, a data deve ser inserida neste formato: 11/11/2011')
    #     return {"nome": nome, "data_nascimento": data_nascimento_obj}

    def selecionar_paciente_tabela(self, dados_paciente, titulo):
        titulos = [dados_paciente[0][0], dados_paciente[0][1], dados_paciente[0][2]]
        sg.theme('Default')
        layout = [[sg.Table(values=dados_paciente[1:][:], headings=titulos, max_col_width=50,
                             # background_color='light blue',
                             def_col_width=200,
                             auto_size_columns=True,
                             display_row_numbers=True,
                             justification='left',
                             alternating_row_color='lightgrey',
                             key='dado',
                             row_height=35,
                             tooltip='This is a table')],
                  [sg.Button('Selecionar', size=(20, 2)), sg.Button('sair', size=(20, 2))],
                  ]
        window = sg.Window(titulo, layout
                           #botao, valores = window.Read()
                           )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'sair':
                break
            elif event == 'Selecionar':
                window.close()
                return values['dado']
        window.close()
        return None

#     def mostrar_paciente(self, dados_paciente):
#         sg.theme('Default')
#         idade_dias = datetime.today().date() - dados_paciente["data_nascimento"]
#         idade = idade_dias.days // 365.24231481481481481481481481481481
#         sg.popup(   f'NOME:         {dados_paciente["nome"]}\n'
#                     f'CPF:          {dados_paciente["cpf"]}\n'
#                     f'IDADE:        {idade:.0f} anos\n'
# #                    f'DOSE:         {dados_paciente["dose"]}\n'
# #                    f'APLICADA:     {dados_paciente["aplicada"]}\n'
#                     )
    def listar_paciente_tabela(self, dados_paciente, titulo):
        titulos = [dados_paciente[0][0], dados_paciente[0][1], dados_paciente[0][2]]
        sg.theme('Default')
        layout = [[sg.Table(values=dados_paciente[1:][:], headings=titulos, max_col_width=50,
                             # background_color='light blue',
                             def_col_width=200,
                             auto_size_columns=True,
                             display_row_numbers=True,
                             justification='left',
                             alternating_row_color='lightgrey',
                             key='dado',
                             row_height=35,
                             tooltip='This is a table')],
                            [sg.Button('ok')]
                            ]
        window = sg.Window(titulo, layout
                           #botao, valores = window.Read()
                           )
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == 'ok':
                break
        window.close()
        return None

    def cpf_ja_cadastrado(self, cpf):
        sg.theme('Default')
        sg.popup(f'O cpf {cpf} já foi cadastrado.', no_titlebar=True)

    def cpf_nao_cadastrado(self, cpf):
        sg.theme('Default')
        sg.popup(f'O cpf {cpf} ainda não foi cadastrado.', no_titlebar=True)

    def nenhum_paciente(self):
        sg.theme('Default')
        sg.popup('Ainda não há pacientes cadastrados.', no_titlebar=True)

    def nenhum_agendamento(self):
        sg.theme('Default')
        sg.popup('Ainda não há atendimentos agendados para nenhum paciente', no_titlebar=True)

    def sucesso(self, nome, cpf=0, data=datetime):
        sg.theme('Default')
        if cpf == 0:
            sg.popup(f'Paciente {nome}, nascido em {data} editado!', no_titlebar=True)
        else:
            sg.popup(f'Paciente {nome}, com cpf {cpf} e nascido em {data} cadastrado!', no_titlebar=True)
