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
        data_nascimento_str = input("Data de nascimento: ")
        data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento_obj}

    def pega_dados_paciente_edicao(self):
        print('--------- EDITAR PACIENTE ----------')
        nome = input('Nome: ')
        data_nascimento_str = input("Data de nascimento: ")
        data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
        return {"nome": nome, "data_nascimento": data_nascimento_obj}

    def selecionar_paciente(self):
        print('---- SELECIONAR PACIENTE ------')
        cpf = input('CPF: ')
        return cpf

    def mostrar_paciente(self, dados_paciente):
        print("--------------------------------")
        print(f'NOME: {dados_paciente["nome"]} |'
              f' CPF: {dados_paciente["cpf"]} |'
              f' DATA DE NASCIMENTO: {dados_paciente["data_nascimento"]}')

    # def mostrar_lista_pacientes(self):
    #     pass

    def mostrar_pacientes_nunca_agendados(self):
        pass

    def mostrar_vacinados_primeira_dose(self):
        pass

    def mostrar_vacinados_segunda_dose(self):
        pass

    def linha(self):
        print("-" * 60)
