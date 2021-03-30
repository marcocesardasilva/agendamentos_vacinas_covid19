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

    def abre_tela(self):
        pass

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False
