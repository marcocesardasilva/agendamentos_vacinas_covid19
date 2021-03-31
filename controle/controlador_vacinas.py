from limite.tela_vacinas import TelaVacinas
from entidade.vacina import Vacina


class ControladorVacinas():

    def __init__(self, controlador_sistema):
        self.__vacinas = []
        self.__tela_vacinas = TelaVacinas()
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def cadastrar_vacina(self, fabricante, quantidade):
        pass

    def adicionar_dose(self, fabricante):
        pass

    def subtrair_dose(self, fabricante):
        pass

    def editar_vacina(self, fabricante, quantidade):
        pass

    def get_vacina(self, fabricante):
        pass

    def listar_doses_disponiveis(self):
        pass

    def listar_doses_aplicadas(self):
        pass

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_vacina,
            2: self.adicionar_dose,
            3: self.subtrair_dose,
            4: self.editar_vacina,
            5: self.listar_doses_disponiveis,
            6: self.listar_doses_aplicadas,
            0: self.retorna_tela_principal
        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_vacinas.tela_opcoes()]()
