from limite.tela_enfermeiros import TelaEnfermeiros
from entidade.enfermeiro import Enfermeiro


class ControladorEnfermeiros():

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_enfermeiros = TelaEnfermeiros(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pacientes = None
        self.__controlador_agendamentos = None
        self.__mantem_tela_aberta = True

    def cadastrar_enfermeiro(self):
        while True:
            dados_enfermeiro = self.__tela_enfermeiros.pegar_dados_enfermeiro()
            for enfermeiro in self.__enfermeiros:
                if enfermeiro.matricula == dados_enfermeiro["matricula"]:
                    self.__tela_enfermeiros.matricula_ja_cadastrada(dados_enfermeiro["matricula"])
                    return None
                elif enfermeiro.cpf == dados_enfermeiro["cpf"]:
                    self.__tela_enfermeiros.cpf_ja_cadastrado(dados_enfermeiro["cpf"])
                    return None
            enfermeiro = Enfermeiro(dados_enfermeiro["nome"],
                                    dados_enfermeiro["cpf"],
                                    dados_enfermeiro["matricula"],
                                    dados_enfermeiro["status"])
            self.__enfermeiros.append(enfermeiro)
            break

    def editar_enfermeiro(self):
        enfermeiro_editar = self.get_enfermeiro()
        while True:
            dados_editar = self.__tela_enfermeiros.pegar_dados_enfermeiro_edicao()
            for enfermeiro in self.__enfermeiros:
                if enfermeiro.matricula == dados_editar["matricula"]:
                    self.__tela_enfermeiros.matricula_ja_cadastrada(dados_editar["matricula"])
                    return None
                elif enfermeiro.cpf == dados_editar["cpf"]:
                    self.__tela_enfermeiros.cpf_ja_cadastrado(dados_editar["cpf"])
                    return None
            break
        for enfermeiro in self.__enfermeiros:
            if enfermeiro == enfermeiro_editar:
                enfermeiro.nome = dados_editar['nome']
                enfermeiro.matricula = dados_editar['matricula']
                enfermeiro.status = "Ativo"

    def consultar_enfermeiro(self):
        enfermeiro_consultar = self.get_enfermeiro()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro == enfermeiro_consultar:
                self.__tela_enfermeiros.mostrar_enfermeiro(
                    {"nome": enfermeiro.nome,
                    "cpf": enfermeiro.cpf,
                    "matricula": enfermeiro.matricula,
                    "status": enfermeiro.status}
                    )

    def get_enfermeiro(self):
        while True:
            matricula = self.__tela_enfermeiros.selecionar_enfermeiro()
            if len(self.__enfermeiros) == 0:
                self.__tela_enfermeiros.enfermeiro_nao_cadastrado()
                break
            for enfermeiro in self.__enfermeiros:
                if matricula == enfermeiro.matricula:
                    return enfermeiro
            self.__tela_enfermeiros.enfermeiro_nao_cadastrado()
            break

    def enfermeiro_inativo(self):
        self.__tela_enfermeiros.enfermeiro_inativo()

    def alterar_status_enfermeiro(self):
        enfermeiro = self.get_enfermeiro()
        status = self.__tela_enfermeiros.status_enfermeiro(enfermeiro.matricula)
        enfermeiro.status = status

    def listar_enfermeiros(self):
        for enfermeiro in self.__enfermeiros:
            self.__tela_enfermeiros.mostrar_enfermeiro(
                {"nome": enfermeiro.nome,
                 "cpf": enfermeiro.cpf,
                 "matricula": enfermeiro.matricula,
                 "status": enfermeiro.status}
            )

    def listar_pacientes_por_enfermeiro(self):
        self.__controlador_pacientes = self.__controlador_sistema.controlador_pacientes
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        enfermeiro = self.get_enfermeiro()
        self.__tela_enfermeiros.mostrar_enfermeiro(
            {"nome": enfermeiro.nome,
             "cpf": enfermeiro.cpf,
             "matricula": enfermeiro.matricula,
             "status": enfermeiro.status}
        )
        for agendamento in self.__controlador_agendamentos.agendamentos:
            if agendamento.enfermeiro == enfermeiro:
                self.__tela_enfermeiros.mostrar_pacientes_por_enfermeiro(
                    {"nome": agendamento.paciente.nome,
                    "cpf": agendamento.paciente.cpf,
                    "data_nascimento": agendamento.paciente.data_nascimento}
                )


    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_enfermeiro,
                        2: self.editar_enfermeiro,
                        3: self.consultar_enfermeiro,
                        4: self.alterar_status_enfermeiro,
                        5: self.listar_enfermeiros,
                        6: self.listar_pacientes_por_enfermeiro,
                        0: self.retorna_tela_principal
                        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_enfermeiros.tela_opcoes()]()
