class TelaPacientes():

    def tela_opcoes(self):
        print("-------- PACIENTES ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar paciente")
        print("2 - Editar paciente")
        print("3 - Consultar paciente")
        print("4 - Listar pacientes cadastrados")
        print("5 - Listar pacientes nunca agendados")
        print("6 - Listar pacientes vacinados 1ª dose")
        print("7 - Listar pacientes vacinados 2ª dose")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pega_dados_paciente(self):
        print("-------- INCLUIR PACIENTE ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de nascimento: ")
        return {"nome": nome, "cpf": cpf, "data de nascimento": data_nascimento}

    def mostrar_paciente(self, dados_paciente):
        print("--------------------------------")
        print("NOME DO PACIENTE: ", dados_paciente["nome"])
        print("CPF DO PACIENTE: ", dados_paciente["cpf"])
        print("DATA DE NASCIMENTO DO PACIENTE: ", dados_paciente["data_nascimento"])