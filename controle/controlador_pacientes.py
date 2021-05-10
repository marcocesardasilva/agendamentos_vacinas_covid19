from limite.tela_pacientes_main import TelaPacientes
from entidade.paciente import Paciente
from controle.controlador_agendamentos import ControladorAgendamentos
from datetime import datetime as datetime
from math import trunc
from persistencia.pacienteDAO import PacienteDAO


class ControladorPacientes():

    def __init__(self, controlador_sistema):
        self.__dao = PacienteDAO()
        self.__tela_pacientes_main = TelaPacientes(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_agendamentos = None
        self.__mantem_tela_aberta = True

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def pacientes(self):
        return self.__dao.get_all()

    def cadastrar_paciente(self):
        while True:
            dados_paciente = self.__tela_pacientes_main.pegar_dados_cadastrar()
            if dados_paciente is None:
                break
            try:
                nome = dados_paciente["nome"].upper()
                if not nome.replace(' ', '').isalpha():
                    break
            except (ValueError, TypeError):
                self.__tela_pacientes_main.mensagem('Houve problemas com o tipo de dado digitado')
            try:
                cpf = dados_paciente["cpf"].replace(' ', '')
                if not cpf.isnumeric() and len(cpf) == 11:
                    self.__tela_pacientes_main.mensagem(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
                    break
            except (ValueError, TypeError):
                self.__tela_pacientes_main.mensagem('Houve problemas com o tipo de dado digitado')
            try:
                data_nascimento_str = dados_paciente["data_nascimento"]
                data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
                idade_dias = datetime.today().date() - data_nascimento_obj
                idade = int(idade_dias.days // 365.24231481481481481481481481481481)
                if not 0 < idade < 150:
                    self.__tela_pacientes_main.mensagem('Idade inválida, a idade deve ser entre 0 e 150 anos')
                    break
            except:
                self.__tela_pacientes_main.mensagem('Data inválida, a data deve ser inserida neste formato: 11/11/2011')
                break
            if len(self.__dao.get_all()) == 0:
                self.__tela_pacientes_main.mensagem(f'Deu certo até aqui{len(self.__dao.get_all())}')

                paciente = Paciente(nome, cpf, data_nascimento_obj)
                self.__dao.add(paciente)
                break
            else:
                for paciente in self.__dao.get_all():
                    if not dados_paciente:
                        self.__tela_pacientes_main.mensagem()
                        return None
                    if dados_paciente["cpf"] == paciente.cpf:
                        self.__tela_pacientes_main.mensagem(f'O cpf {dados_paciente["cpf"]} já foi cadastrado')
                        return None
                paciente = Paciente(nome, cpf, data_nascimento_obj)
                self.__dao.add(paciente)
                self.__tela_pacientes_main.sucesso(nome, cpf, data_nascimento_obj)
                break

    # def cadastrar_paciente(self):
    #     while True:
    #         dados_paciente = self.__tela_pacientes.pega_dados_paciente()
    #         if len(self.__dao.get_all()) == 0:
    #             paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
    #             self.__dao.add(paciente)
    #             break
    #         else:
    #             for paciente in self.__dao.get_all():
    #                 if dados_paciente["cpf"] == paciente.cpf:
    #                     self.__tela_pacientes.cpf_ja_cadastrado(dados_paciente['cpf'])
    #                     return None
    #             paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
    #             self.__dao.add(paciente)
    #             self.__tela_pacientes.sucesso(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
    #             break

    def editar_paciente(self, nome=0, cpf=0, data_nascimento=0):
        # paciente_editar = self.__dao.get('cpf')
        paciente_editar = self.get_paciente()
        # rever
        if paciente_editar is None:
            return None
        dados_editar = self.__tela_pacientes_main.pegar_dados_cadastrar()
        try:
            nome = dados_editar["nome"].upper()
            if nome.replace(' ', '').isalpha():
                nome_ok = nome
        except (ValueError, TypeError):
            self.__tela_pacientes_main.mensagem('Houve problemas com o tipo de dado digitado')
            return None
        try:
            data_nascimento_str = dados_editar["data_nascimento"]
            data_nascimento_obj = datetime.strptime(data_nascimento_str, '%d/%m/%Y').date()
            idade_dias = datetime.today().date() - data_nascimento_obj
            idade = int(idade_dias.days // 365.24231481481481481481481481481481)
            if not 0 < idade < 150:
                self.__tela_pacientes_main.mensagem('Idade inválida, a idade deve ser entre 0 e 150 anos')
                return None
        except:
            self.__tela_pacientes_main.mensagem('Data inválida, a data deve ser inserida neste formato: 11/11/2011')
        paciente_editar.nome = nome_ok
        paciente_editar.data_nascimento = data_nascimento_obj
        self.__dao.add(paciente_editar)
        self.__tela_pacientes_main.sucesso(paciente_editar.nome, paciente_editar.cpf, data_nascimento_obj)

    # def consultar_paciente(self):
    #     self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
    #     paciente_consultar = self.get_paciente()
    #     dose = 0
    #     aplicada = False
    #     for agendamento in self.__controlador_agendamentos.agendamentos:
    #         for paciente in self.__dao.get_all():
    #             if agendamento.paciente == paciente:
    #                 dose = agendamento.dose
    #                 aplicada = agendamento.aplicada
    #     for paciente in self.__dao.get_all():
    #         if paciente_consultar == paciente:
    #             self.__tela_pacientes_main.mostrar_paciente(
    #                 {"nome": paciente.nome,
    #                  "cpf": paciente.cpf,
    #                  "data_nascimento": paciente.data_nascimento,
    #                  "dose": dose,
    #                  "aplicada": aplicada
    #                  }
    #             )

    def get_paciente(self):
        if len(self.__dao.get_all()) == 0:
            self.__tela_pacientes_main.nenhum_paciente()
            return None
        else:
            cpf = self.selecionar_lista_pacientes()
            if cpf is None:
                return None
            if self.__dao.get(cpf):
                return self.__dao.get(cpf)
            else:
                self.__tela_pacientes_main.cpf_nao_cadastrado(cpf)
        return None

    # def get_paciente_cpf(self):
    #     if len(self.__dao.get_all()) == 0:
    #         self.__tela_pacientes_main.nenhum_paciente()
    #         return None
    #     else:
    #         cpf = self.listar_pacientes()
    #         if cpf is None:
    #             return None
    #         if self.__dao.get(cpf):
    #             return self.__dao.get(cpf)
    #         else:
    #             self.__tela_pacientes_main.cpf_nao_cadastrado(cpf)
    #     return None

    def tabela_pacientes(self):
        matriz = []
        linha = ['      Nome       ', '      CPF      ', ' Idade ']
        matriz.append(linha)
        for paciente in self.__dao.get_all():
            linha = [paciente.nome, paciente.cpf]
            idade_dias = datetime.today().date() - paciente.data_nascimento
            idade = idade_dias.days // 365.24231481481481481481481481481481
            linha.append(idade)
            matriz.append(linha)
        return matriz

    def selecionar_lista_pacientes(self):
        matriz = []
        linha = ['        Nome        ', '    CPF    ', 'Idade']
        matriz.append(linha)
        if len(self.__dao.get_all()) == 0:
            self.__tela_pacientes_main.nenhum_paciente()
            return None
        for paciente in self.__dao.get_all():
            linha = [paciente.nome, paciente.cpf]
            idade_dias = datetime.today().date() - paciente.data_nascimento
            idade = idade_dias.days // 365.24231481481481481481481481481481
            linha.append(idade)
            matriz.append(linha)
        paciente_selecionado = self.__tela_pacientes_main.selecionar_paciente_tabela(matriz, 'Selecionar Pacientes')
        if paciente_selecionado:
            return matriz[paciente_selecionado[0] + 1][1]

    def listar_pacientes(self):
        matriz = []
        linha = ['        Nome        ', '    CPF    ', 'Idade']
        matriz.append(linha)
        if len(self.__dao.get_all()) == 0:
            self.__tela_pacientes_main.nenhum_paciente()
            return None
        for paciente in self.__dao.get_all():
            linha = [paciente.nome, paciente.cpf]
            idade_dias = datetime.today().date() - paciente.data_nascimento
            idade = idade_dias.days // 365.24231481481481481481481481481481
            linha.append(idade)
            matriz.append(linha)
        self.__tela_pacientes_main.listar_paciente_tabela(matriz, 'Lista de pacientes')

    # def listar_pacientes(self):
    #     for paciente in self.__dao.get_all():
    #         self.__tela_pacientes_main.mostrar_paciente(
    #         {"nome": paciente.nome,
    #         "cpf": paciente.cpf,
    #         "data_nascimento": paciente.data_nascimento}
    #                     )

    def listar_pacientes_nao_agendados(self):
        pacientes_agendados = []
        matriz = []
        linha = ['        Nome        ', '    CPF    ', 'Idade']
        matriz.append(linha)
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                raise Exception
            for agendamento in self.__controlador_agendamentos.agendamentos:
                for paciente in self.__dao.get_all():
                    if agendamento.paciente.cpf == paciente.cpf:
                        pacientes_agendados.append(paciente)
            for paciente in self.__dao.get_all():
                if paciente not in pacientes_agendados:
                    linha = [paciente.nome, paciente.cpf]
                    idade_dias = datetime.today().date() - paciente.data_nascimento
                    idade = idade_dias.days // 365.24231481481481481481481481481481
                    linha.append(idade)
                    matriz.append(linha)
            #paciente_selecionado = \
            self.__tela_pacientes_main.listar_paciente_tabela(matriz, 'Pacientes aguardando agendamento')
            # if paciente_selecionado:
            #     return matriz[paciente_selecionado[0] + 1][1]
        except Exception:
            self.__tela_pacientes_main.nenhum_agendamento()

    def pacientes_aguardando_vacina(self):
        pacientes_com_agendamento = 0
        pacientes_total = len(self.__dao.get_all())
        pacientes_sem_agendamento = 0
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__dao.get_all()) == 0:
                return 0
            for agendamento in self.__controlador_agendamentos.agendamentos:
                if agendamento.aplicada == True and agendamento.dose == 1:
                    pacientes_com_agendamento += 1
            pacientes_sem_agendamento = pacientes_total - pacientes_com_agendamento
        except:
            self.__tela_pacientes_main.nenhum_agendamento()
        return pacientes_sem_agendamento

    def listar_pacientes_primeira_dose(self):
        doses_aplicadas = 0
        matriz = [['        Nome        ', '    CPF    ', 'Idade']]
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        # try:
        if len(self.__controlador_agendamentos.agendamentos) == 0:
            raise Exception
        for agendamento in self.__controlador_agendamentos.agendamentos:
            if agendamento.dose == 1:
                if agendamento.aplicada:
                    doses_aplicadas +=1
                    linha = [agendamento.paciente.nome, agendamento.paciente.cpf]
                    idade_dias = datetime.today().date() - agendamento.paciente.data_nascimento
                    idade = idade_dias.days // 365.24231481481481481481481481481481
                    linha.append(idade)
                    matriz.append(linha)
        # paciente_selecionado = \
        if doses_aplicadas == 0:
            self.__tela_pacientes_main.mensagem('Nenhum paciente recebeu a primeira dose')
            return None
        self.__tela_pacientes_main.listar_paciente_tabela(matriz, 'Pacientes que receberam a primeira dose')
            # if paciente_selecionado:
            #     return matriz[paciente_selecionado[0] + 1][1]
        # except Exception:
        #     self.__tela_pacientes_main.nenhum_agendamento()

    def listar_pacientes_segunda_dose(self):
        doses_aplicadas = 0
        matriz = []
        matriz.append(['        Nome        ', '    CPF    ', 'Idade'])
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                raise Exception
            for agendamento in self.__controlador_agendamentos.agendamentos:
                if agendamento.dose == 2:
                    if agendamento.aplicada:
                        doses_aplicadas += 1
                        linha = [agendamento.paciente.nome, agendamento.paciente.cpf]
                        idade_dias = datetime.today().date() - agendamento.paciente.data_nascimento
                        idade = idade_dias.days // 365.24231481481481481481481481481481
                        linha.append(idade)
                        matriz.append(linha)
                    # paciente_selecionado = \
            if doses_aplicadas == 0:
                self.__tela_pacientes_main.mensagem('Nenhum paciente recebeu a segunda dose')
                return None
            self.__tela_pacientes_main.listar_paciente_tabela(matriz, 'Pacientes que receberam a segunda dose')
                    # if paciente_selecionado:
                    #     return matriz[paciente_selecionado[0] + 1][1]
        except Exception:
            self.__tela_pacientes_main.nenhum_agendamento()

    def remover_paciente(self):
        paciente = self.get_paciente()
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        for agendamento in self.__controlador_agendamentos.agendamentos:
            if agendamento.paciente == paciente:
                return None
        if paciente is not None:
            self.__dao.remove(paciente.cpf)

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_paciente,
                        2: self.editar_paciente,
                        3: self.listar_pacientes,
                        4: self.listar_pacientes_nao_agendados,
                        5: self.listar_pacientes_primeira_dose,
                        6: self.listar_pacientes_segunda_dose,
                        7: self.remover_paciente,
                        0: self.retorna_tela_principal}

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_pacientes_main.tela_opcoes()]()
