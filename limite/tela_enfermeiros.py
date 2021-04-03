class TelaEnfermeiros():

    def __init__(self, controlador_enfermeiros):
        self.__controlador_enfermeiros = controlador_enfermeiros

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
        while True:
            try:
                opcao = int(input("Escolha a opcao:"))
                if 0 <= opcao <= 6:
                    return opcao
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
    
    def pegar_dados_enfermeiro(self):
        print("-------- INCLUIR ENFERMEIRO ----------")
        nome = input("Nome: ")
        cpf = input("CPF (apenas números): ")
        matricula = input("Matrícula (4 dígitos): ")
        return {"nome": nome, "cpf": cpf, "matricula": matricula, "status": "Ativo"}

    def pegar_dados_enfermeiro_edicao(self):
        print("-------- EDITAR ENFERMEIRO ----------")
        nome = input('Nome: ')
        matr = input('Matrícula (4 dígitos): ')
        return {'nome': nome, 'matricula': matr}

    def selecionar_enfermeiro(self):
        print('----- SELECIONAR ENFERMEIRO -----')
        matricula = input("Matrícula: ")
        return matricula


    def mostrar_enfermeiro(self, dados_enfermeiro):
        self.linha()
        print(f'NOME: {dados_enfermeiro["nome"]} |'
              f' CPF: {dados_enfermeiro["cpf"]} |'
              f' MATRÍCULA: {dados_enfermeiro["matricula"]} |'
              f' STATUS: {dados_enfermeiro["status"]}'
              )
        self.linha()

    def alterar_status_enfermeiro(self):
        pass

    def mostrar_lista_enferemrios(self, dados_enfermeiro):
        print(
            f'NOME: {dados_enfermeiro["nome"]} |'
            f' CPF: {dados_enfermeiro["cpf"]} |'
            f' MATRÍCULA: {dados_enfermeiro["data_nascimento"]}')

    def mostrar_pacientes_por_enfermeiro(self, dados_paciente):
        print(f'NOME: {dados_paciente["nome"]} |'
              f' CPF: {dados_paciente["cpf"]} |'
              f' DATA DE NASCIMENTO: {dados_paciente["data_nascimento"]}')

    def linha(self):
        print("-" * 70)

    def enfermeiro_nao_cadastrado(self):
        print("Enfermeiro não cadastrado para o código digitado.")
    
    def enfermeiro_inativo(self):
        print("Enfermeiro selecionado inativo.")
