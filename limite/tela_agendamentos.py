from datetime import datetime

class TelaAgendamentos():

    def __init__(self, controlador_agendamento):
        self.__controlador_agendamento = controlador_agendamento

    def tela_opcoes(self):
        print("-------- AGENDAMENTOS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar agendamento")
        print("2 - Consultar agendamento")
        print("3 - Editar agendamento")
        print("4 - Aplicar Vacina")
        print("5 - Remover agendamento")
        print("6 - Listar aplicações agendadas")
        print("7 - Listar histórico de vacinações")
        print("8 - Relatório Geral")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input("Escolha a opcao:"))
                if 0 <= opcao <= 8:
                    return opcao
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
    
    def pegar_dados_cadastrar(self):
        print("-------- CADASTRAR AGENDAMENTO ----------")
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
                opcao = int(input("Qual a dose da vacina (1 - Primeira / 2 - Segunda): "))
                if opcao == 1 or opcao == 2:
                    dose = opcao
                    break
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
        return {"data": data, "horario": horario, "dose": dose}
    
    def agendamento_cadastrado(self):
        print("Agendamento cadastrado com sucesso!")

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
        print("-------- DADOS DO AGENDAMENTO SOLICITADO ----------")
        print("Enfermeiro:", dados_agendamento["enfermeiro"])
        print("Paciente:", dados_agendamento["paciente"])
        print("Vacina:", dados_agendamento["vacina"])
        print("Data:", dados_agendamento["data"])
        print("Horario:", dados_agendamento["horario"])
        print("Dose:", dados_agendamento["dose"])
        print("Status:", dados_agendamento["status"])

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
                opcao = int(input("Qual a dose da vacina (1 - Primeira / 2 - Segunda): "))
                if opcao == 1 or opcao == 2:
                    dose = opcao
                    break
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
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
        return {"data": data, "horario": horario, "dose": dose, "aplicada": aplicada}

    def agendamento_editado(self):
        print("Agendamento editado com sucesso!")

    def vacina_aplicada(self):
        print("Vacina foi aplicada.")
    
    def agendamento_removido(self):
        print("O agendamento solicitado foi removido.")

    def mostrar_lista_agendamentos(self, dados_agendamento):
        print("----------------------------------------")
        print("Enfermeiro:", dados_agendamento["enfermeiro"])
        print("Paciente:", dados_agendamento["paciente"])
        print("Vacina:", dados_agendamento["vacina"])
        print("Data:", dados_agendamento["data"])
        print("Horario:", dados_agendamento["horario"])
        print("Dose:", dados_agendamento["dose"])

    def ja_castrado_primeira_dose(self):
        print("Já existe um agendamento da primeira dose cadastrado para este paciente.")
    
    def ja_castrado_segunda_dose(self):
        print("Já existe um agendamento da segunda dose cadastrado para este paciente.")
    
    def data_recente_primeira_dose(self):
        print("Não agendado! Segunda dose deve ser agendada para 20 dias após a aplicação da primeira dose.")
    
    def nao_castrado_primeira_dose(self):
        print("Não agendado! Segunda dose só pode ser agendada após o agendamento da primeira dose.")

    def agendamento_nao_cadastrado(self):
        print("Agendamento não cadastrado.")

    def agendamento_aberto_nao_cadastrado(self):
        print("Nenhum agendamento aberto foi encontrado.")

    def agendamento_efetivado_nao_cadastrado(self):
        print("Nenhum agendamento efetivado foi encontrado.")

    def mostrar_relatorio(self,dados_relatorio):
        print("------------ RELATÓRIO GERAL --------------")
        print("Total de vacinas aplicadas:              {}".format(dados_relatorio["vacinas_aplicadas"]))
        print("Total de pacientes vacinados 1ª dose:    {}".format(dados_relatorio["paciente_vacinados_primeira_dose"]))
        print("Total de pacientes vacinados 2ª dose:    {}".format(dados_relatorio["paciente_vacinados_segunda_dose"]))
        print("Pacientes aguardando agendamento:        {}".format(dados_relatorio["pacientes_sem_agendamentos"]))
        print("-------------------------------------------")
