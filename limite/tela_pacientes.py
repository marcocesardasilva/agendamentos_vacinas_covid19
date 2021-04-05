from datetime import datetime as datetime

class TelaPacientes():

    def __init__(self, controlador_pacientes):
        self.__controlador_pacientes = controlador_pacientes

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
        while True:
            try:
                opcao = int(input("Escolha a opcao:"))
                if 0 <= opcao <= 7:
                    return opcao
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")

    def pega_dados_paciente(self):
        print("-------- INCLUIR PACIENTE ----------")
        while True:
            try:
                nome = input("Nome: ").upper()
                if nome.replace(' ','').isalpha():
                    break
                else:
                    print(f'O nome {nome} é inválido!')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        while True:
            try:
                cpf = input("CPF (apenas números): ").replace(' ','')
                if cpf.isnumeric() and len(cpf) == 11:
                    break
                else:
                    print(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        while True:
            try:
                data_nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")
                data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
                idade_dias = datetime.today().date() - data_nascimento_obj
                idade = int(idade_dias.days // 365.24231481481481481481481481481481)
                if 0 < idade < 150:
                    break
                else:
                    print('Idade inválida, a idade deve ser entre 0 e 150 anos')

            except:
                print('Data inválida, a data deve ser inserida neste formato: 11/11/2011')
        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento_obj}

    def pega_dados_paciente_edicao(self):
        print('---------- EDITAR PACIENTE ----------')
        while True:
            try:
                nome = input("Nome: ").upper()
                if nome.replace(' ','').isalpha():
                    break
                else:
                    print(f'O nome {nome} é inválido!')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        while True:
            try:
                data_nascimento_str = input("Data de nascimento (dd/mm/aaaa): ")
                data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
                idade_dias = datetime.today().date() - data_nascimento_obj
                idade = int(idade_dias.days // 365.24231481481481481481481481481481)
                if 0 < idade < 150:
                    break
                else:
                    print('Idade inválida, a idade deve ser entre 0 e 150 anos')

            except:
                print('Data inválida, a data deve ser inserida neste formato: 11/11/2011')
        return {"nome": nome, "data_nascimento": data_nascimento_obj}

    def selecionar_paciente(self):
        print('---- SELECIONAR PACIENTE ------')
        while True:
            try:
                cpf = input("CPF (apenas números): ").replace(' ','')
                if cpf.isnumeric() and len(cpf) == 11:
                    break
                else:
                    print(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
            except (ValueError, TypeError):
                print('Houve problemas com o tipo de dado digitado')
        return cpf

    def mostrar_paciente(self, dados_paciente):
        self.linha()
        idade_dias = datetime.today().date() - dados_paciente["data_nascimento"]
        idade = idade_dias.days // 365.24231481481481481481481481481481
        print(f'NOME: {dados_paciente["nome"]} |'
              f' CPF: {dados_paciente["cpf"]} |'
              f' Idade: {idade:.0f} anos')

    def linha(self):
        print("-" * 90)

    def cpf_ja_cadastrado(self, cpf):
        print(f'O cpf {cpf} já foi cadastrado.')

    def cpf_nao_cadastrado(self, cpf):
        print(f'O cpf {cpf} ainda não foi cadastrado.')

    def nenhum_paciente(self):
        print('Ainda não há pacientes cadastrados.')

    def nenhum_agendamento(self):
        print('Ainda não há atendimentos agendados para nenhum paciente')

    def sucesso(self, nome, cpf=0, data=datetime):
        self.linha()
        if cpf == 0:
            print(f'Paciente {nome}, nascido em {data} editado!')
        else:
            print(f'Paciente {nome}, com cpf {cpf} e nascido em {data} cadastrado!')
        self.linha()