class TelaAgendamentos():

    def tela_opcoes(self):
        print("-------- AGENDAMENTOS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar agendamento")
        print("2 - Editar agendamento")
        print("3 - Consultar agendamento")
        print("4 - Remover agendamento")
        print("5 - Listar aplicações agendadas")
        print("6 - Listar histórico de vacinações")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pegar_dados_agendamento(self):
        print("-------- DADOS AGENDAMENTO ----------")
        data = input("Data (dd/mm/aaaa): ")
        hora = input("Hora (hh:mm):")
        dose = int(input("Dose (1 - Primeira / 2 - Segunda): "))
        return {"data_hora_agendamento": data+" "+hora, "dose": dose}

    def selecionar_agendamento(self):
        pass

    def mostrar_agendamento(self):
        pass

    def mostrar_agendamentos_abertos(self):
        pass

    def mostrar_aplicacoes_efetivadas(self):
        pass
