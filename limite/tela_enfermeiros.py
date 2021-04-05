from datetime import datetime as datetime


class TelaEnfermeiros():

    def __init__(self, controlador_enfermeiros):
        self.__controlador_enfermeiros = controlador_enfermeiros

    def tela_opcoes(self):
        print("-------- ENFERMEIROS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar enfermeiro")
        print("2 - Editar enfermeiro")
        print("3 - Consultar enfermeiro")
        print("4 - Alterar status do enfermeiro")
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

    def status_enfermeiro(self, matricula):
        print(f"Alterar status do enfermeiro {matricula}: ")
        while True:
            try:
                print("Para definir status como <Ativo> digite 1,\nPara definir status como <Inativo> digite 2")
                status_desejado = int(input('Status: '))
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