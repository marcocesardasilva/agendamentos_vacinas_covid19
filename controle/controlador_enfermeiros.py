from limite.tela_enfermeiros import TelaEnfermeiros
from entidade.enfermeiro import Enfermeiro


class ControladorEnfermeiros():

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_enfermeiros = TelaEnfermeiros(self)
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def cadastrar_enfermeiro(self):
        dados_enfermeiro = self.__tela_enfermeiros.pegar_dados_enfermeiro()
        enfermeiro = Enfermeiro(dados_enfermeiro["nome"],
                                dados_enfermeiro["cpf"],
                                dados_enfermeiro["matricula"],
                                dados_enfermeiro["status"])
        self.__enfermeiros.append(enfermeiro)

    def editar_enfermeiro(self):
        enfermeiro_editar = self.get_enfermeiro()
        dados_editar = self.__tela_enfermeiros.pegar_dados_enfermeiro_edicao()
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
        matricula = self.__tela_enfermeiros.selecionar_enfermeiro()
        for enfermeiro in self.__enfermeiros:
            if matricula == enfermeiro.matricula:
                salvar_enfermeiro = enfermeiro
                return salvar_enfermeiro

    def remover_enfermeiro(self):
        enfermeiro_editar = self.get_enfermeiro()
        for enfermeiro in self.__enfermeiros:
            if enfermeiro == enfermeiro_editar:
                enfermeiro.status = "Inativo"

    def listar_enfermeiros(self):
        for enfermeiro in self.__enfermeiros:
            self.__tela_enfermeiros.mostrar_enfermeiro(
                {"nome": enfermeiro.nome,
                 "cpf": enfermeiro.cpf,
                 "matricula": enfermeiro.matricula,
                 "status": enfermeiro.status}
            )

    def listar_pacientes_por_enfermeiro(self):
        pass

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_enfermeiro,
                        2: self.editar_enfermeiro,
                        3: self.consultar_enfermeiro,
                        4: self.remover_enfermeiro,
                        5: self.listar_enfermeiros,
                        6: self.listar_pacientes_por_enfermeiro,
                        0: self.retorna_tela_principal
                        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_enfermeiros.tela_opcoes()]()
