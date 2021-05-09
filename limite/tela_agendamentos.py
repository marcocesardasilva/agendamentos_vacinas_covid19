from datetime import datetime
import PySimpleGUI as sg

class TelaAgendamentos():

    def __init__(self, controlador_agendamento):
        self.__controlador_agendamento = controlador_agendamento

    def tela_opcoes(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Selecione a opção desejada', size=(30, 1))],
            [sg.Button('Cadastrar agendamento', size=(30, 2), key='1')],
            [sg.Button('Consultar agendamento', size=(30, 2), key='2')],
            [sg.Button('Editar agendamento', size=(30, 2), key='3')],
            [sg.Button('Aplicar Vacina', size=(30, 2), key='4')],
            [sg.Button('Remover agendamento', size=(30, 2), key='5')],
            [sg.Button('Listar aplicações agendadas', size=(30, 2), key='6')],
            [sg.Button('Listar histórico de vacinações', size=(30, 2), key='7')],
            [sg.Button('Relatório Geral', size=(30, 2), key='8')],
            [sg.Button('Retornar', size=(30, 2), key='0')]
        ]
        window = sg.Window('Agendamentos',size=(800, 480)).Layout(layout)
        botao, _ = window.Read()
        opcao = int(botao)
        window.close()
        return opcao
    
    def pegar_dados_cadastrar(self):
        sg.theme('Default')
        layout = [
            [sg.Text('Cadastrar Agendamento:')],
            [sg.Text('Data (dd/mm/aaaa):',size=(15, 1)), sg.InputText()],
            [sg.Text('Horário (hh:mm):',size=(15, 1)), sg.InputText()],
            #[sg.Text('Dose da vacina (1 ou 2):',size=(15, 1)), sg.InputText()],
            [sg.Text('Dose', size=(15,1)), sg.InputCombo(('1ª dose', '2ª dose'), size=(15,1))],
            # [sg.Text('Dose', size=(15,1)), sg.Radio('1ª dose', "Radio", default=True),
            #     sg.Radio('2ª dose', "Radio")],
            [sg.Button('Ok'), sg.Button('Cancelar')]
        ]
        window = sg.Window('Agendamentos',size=(800, 480)).Layout(layout)
        while True:
            try:
                event, values = window.read()
                print(values[0])
                print(values[1])
                print(values[2])
                if event == sg.WIN_CLOSED or event == 'Cancelar':
                    window.close()
                    return None
                data_str = values[0]
                data = datetime.strptime(data_str, '%d/%m/%Y').date()
                horario_str = values[1]
                horario = datetime.strptime(horario_str, '%H:%M').time()
                datetime.strptime("08:00", '%H:%M').time() <= horario <= datetime.strptime("18:00", '%H:%M').time()
                break
            except ValueError:
                sg.popup('Valores digitados inválidos.', 'Tente novamente.')
        if values[2] == '1ª dose':
            dose = 1
        if values[2] == '2ª dose':
            dose = 2
        window.close()
        return {"data": data, "horario": horario, "dose": dose}

    def selecionar_agendamento(self):
        print('----- SELECIONAR AGENDAMENTO -----')
        while True:
            try:
                opcao = int(input("Qual a dose da vacina (1 - Primeira / 2 - Segunda): "))
                if opcao == 1 or opcao == 2:
                    dose = opcao
                    break
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
        return dose

    def mostrar_agendamento(self, dados_agendamento):
        print("--------- DADOS DO AGENDAMENTO SOLICITADO -----------")
        print("Enfermeiro:  ", dados_agendamento["enfermeiro"])
        print("Paciente:    ", dados_agendamento["paciente"])
        print("Vacina:      ", dados_agendamento["vacina"])
        print("Data:        ", dados_agendamento["data"])
        print("Horario:     ", dados_agendamento["horario"])
        print("Dose:        ", dados_agendamento["dose"])
        print("Status:      ", dados_agendamento["status"])

    def pegar_dados_editar(self):
        print("-------- EDITAR AGENDAMENTO ----------")
        while True:
            try:
                data_str = input("Data (dd/mm/aaaa): ")
                data = datetime.strptime(data_str, '%d/%m/%Y').date()
                if data:
                    break
            except:
                print('Data inválida! A data deve ser inserida neste formato: dd/mm/aaaa.')
        while True:
            try:
                horario_str = input("Horário (hh:mm):")
                horario = datetime.strptime(horario_str, '%H:%M').time()
                if datetime.strptime("08:00", '%H:%M').time() <= horario <= datetime.strptime("18:00", '%H:%M').time():
                    break
                else:
                    raise Exception
            except Exception:
                print('Horário inválido! O horário deve ser comercial (08:00 às 18:00).')
        while True:
            try:
                opcao = int(input("Vacina já foi aplicada (1 - Não / 2 - Sim): "))
                if opcao == 1 or opcao == 2:
                    status_aplicacao = opcao
                    break
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
        aplicada = False
        if status_aplicacao == 2:
            aplicada = True
        return {"data": data, "horario": horario, "aplicada": aplicada}

    def mostrar_lista_agendamentos(self, dados_agendamento):
        print("----------------------------------------")
        print("Enfermeiro:", dados_agendamento["enfermeiro"])
        print("Paciente:", dados_agendamento["paciente"])
        print("Vacina:", dados_agendamento["vacina"])
        print("Data:", dados_agendamento["data"])
        print("Horario:", dados_agendamento["horario"])
        print("Dose:", dados_agendamento["dose"])
        print("Código:", dados_agendamento["codigo"])
    
    def mostrar_relatorio(self,dados_relatorio):
        sg.theme('Default')
        dados = [
            ['Total de vacinas aplicadas:', dados_relatorio['vacinas_aplicadas']],
            ['Total de pacientes vacinados 1ª dose:', dados_relatorio['paciente_vacinados_primeira_dose']],
            ['Total de pacientes vacinados 2ª dose:', dados_relatorio['paciente_vacinados_segunda_dose']],
            ['Pacientes não vacinados:', dados_relatorio['pacientes_sem_agendamentos']]
        ]
        headings = ['            Indicador            ', '    Contador    ']
        layout = [
            [sg.Table(values=dados, headings=headings, max_col_width=10,
                #background_color='light blue',
                auto_size_columns=True,
                display_row_numbers=False,
                justification='left',
                num_rows=4,
                #alternating_row_color='lightblue',
                key='-TABLE-',
                row_height=50,
                tooltip='Relatório de Indicadores de Vacinas')],
                [sg.Button('Ok')]
        ]
        window = sg.Window('Agendamentos',size=(800, 480)).Layout(layout)
        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED or event == 'Ok':
                break
        window.close()

    def agendamento_cadastrado(self):
        sg.theme('Default')
        sg.popup("Agendamento cadastrado com sucesso!")
    
    def agendamento_editado(self):
        sg.theme('Default')
        sg.popup("Agendamento editado com sucesso!")

    def vacina_aplicada(self):
        sg.theme('Default')
        sg.popup("Vacina foi aplicada.")
    
    def agendamento_removido(self):
        sg.theme('Default')
        sg.popup("O agendamento solicitado foi removido.")

    def ja_castrado_primeira_dose(self):
        sg.theme('Default')
        sg.popup('Já existe um agendamento da primeira dose cadastrado para este paciente.')
    
    def ja_castrado_segunda_dose(self):
        sg.theme('Default')
        sg.popup('Já existe um agendamento da segunda dose cadastrado para este paciente.')
    
    def data_recente_primeira_dose(self):
        sg.theme('Default')
        sg.popup('Não agendado! Segunda dose deve ser agendada para 20 dias após a aplicação da primeira dose.')
    
    def nao_castrado_primeira_dose(self):
        sg.theme('Default')
        sg.popup('Não agendado! Segunda dose só pode ser agendada após o agendamento da primeira dose.')

    def agendamento_nao_cadastrado(self):
        sg.theme('Default')
        sg.popup('Agendamento não cadastrado.')

    def agendamento_aberto_nao_cadastrado(self):
        sg.theme('Default')
        sg.popup('Nenhum agendamento aberto foi encontrado.')

    def agendamento_efetivado_nao_cadastrado(self):
        sg.theme('Default')
        sg.popup('Nenhum agendamento efetivado foi encontrado.')
    
    def lista_vazia(self):
        sg.theme('Default')
        sg.popup('Não existem agendamentos cadastradas no sistema.')
