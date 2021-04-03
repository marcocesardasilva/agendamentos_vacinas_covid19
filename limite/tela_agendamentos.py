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
        print("4 - Remover agendamento")
        print("5 - Listar aplicações agendadas")
        print("6 - Listar histórico de vacinações")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input("Escolha a opcao:"))
                if 0 <= opcao <= 6:
                    return opcao
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
    
    def pegar_dados_agendamento(self):
        print("-------- DADOS AGENDAMENTO ----------")
        data = input("Data (dd/mm/aaaa): ")
        hora = input("Hora (hh:mm):")
        dose = int(input("Dose (1 - Primeira / 2 - Segunda): "))
        return {"data_hora_agendamento": data+" "+hora, "dose": dose}

    def selecionar_agendamento(self):
        while True:
            try:
                digitado = input("CPF do Paciente (apenas números): ")
                if len(digitado) == 11:
                    cpf = digitado
                    break
                else:
                    print("CPF digitado inválido! Digite apenas números.")
            except ValueError:
                print("Caracterie digitado inválido para CPF!")
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
        return {"cpf": cpf, "dose": dose}

    def mostrar_agendamento(self, dados_agendamento):
        print("----------------------------------------")
        print("Enfermeiro:", dados_agendamento["enfermeiro"])
        print("Paciente:", dados_agendamento["paciente"])
        print("Vacina:", dados_agendamento["vacina"])
        print("Data e Hora:", dados_agendamento["data_hora_agendamento"])
        print("Dose:", dados_agendamento["dose"])
        print("Status:", dados_agendamento["status"])

    def mostrar_lista_agendamentos(self, dados_agendamento):
        print("----------------------------------------")
        print("Enfermeiro:", dados_agendamento["enfermeiro"])
        print("Paciente:", dados_agendamento["paciente"])
        print("Vacina:", dados_agendamento["vacina"])
        print("Data e Hora:", dados_agendamento["data_hora_agendamento"])
        print("Dose:", dados_agendamento["dose"])
