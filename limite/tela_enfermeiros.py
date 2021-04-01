class TelaEnfermeiros():

    def tela_opcoes(self):
        print("-------- ENFERMEIROS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar enfermeiro")
        print("2 - Editar enfermeiro")
        print("3 - Consultar enfermeiro")
        print("4 - Remover enfermeiro")
        print("5 - Listar enfermeiros")
        print("6 - Listar pacientes atendidos por um determinado enfermeiro")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao
    
    def pegar_dados_enfermeiro(self):
        print("-------- INCLUIR ENFERMEIRO ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        matricula = input("Matrícula: ")
        return {"nome": nome, "cpf": cpf, "matricula": matricula, "status": "Ativo"}

    def selecionar_enfermeiro(self):
        print('----- SELECIONAR ENFERMEIRO -----')
        matricula = input("Matrícula: ")
        return matricula

    def mostrar_enfermeiro(self, dados_enfermeiro):
        print(f'NOME: {dados_enfermeiro["nome"]} |'
              f' CPF: {dados_enfermeiro["cpf"]} |'
              f' MATRÍCULA: {dados_enfermeiro["matricula"]} |'
              f' STATUS: {dados_enfermeiro["status"]}'
              )

    def alterar_status_enfermeiro(self):
        pass

    def mostrar_lista_enferemrios(self, dados_enfermeiro):
        print(
            f'NOME: {dados_enfermeiro["nome"]} |'
            f' CPF: {dados_enfermeiro["cpf"]} |'
            f' MATRÍCULA: {dados_enfermeiro["data_nascimento"]}')

    def mostrar_pacientes_por_enfermeiro(self):
        pass

    def linha(self):
        print("-" * 60)