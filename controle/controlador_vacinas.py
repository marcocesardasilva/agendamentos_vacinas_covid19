from limite.tela_vacinas import TelaVacinas
from entidade.vacina import Vacina


class ControladorVacinas():

    def __init__(self, controlador_sistema):
        self.__vacinas = []
        self.__tela_vacinas = TelaVacinas(self)
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def cadastrar_vacina(self, fabricante, quantidade):
        dados_vacina = self.__tela_vacinas.pegar_dados_vacina()
        vacina = Vacina(dados_vacina["fabricante"], dados_vacina["quantidade"])
        self.__vacinas.append(vacina)

    def adicionar_dose(self):
        fabricante = self.get_vacina()
        quantidade = self.__tela_vacinas.pegar_quantidade()
        self.__vacinas[fabricante].quantidade += quantidade

    def subtrair_dose(self, fabricante):
        fabricante = self.get_vacina()
        quantidade = self.__tela_vacinas.pegar_quantidade()
        self.__vacinas[fabricante].quantidade -= quantidade

    def editar_vacina(self, fabricante, quantidade):
        fabricante = self.get_vacina()
        dados_vacina = self.__tela_vacinas.pegar_dados_vacina()
        self.__vacinas[fabricante].fabricante = dados_vacina["fabricante"]
        self.__vacinas[fabricante].quantidade = dados_vacina["quantidade"]

    def get_vacina(self):
        encontrado = None
        while encontrado is None:
            fabricante = self.__tela_vacinas.selecionar_vacina()
            if fabricante in self.__vacinas:
                encontrado = True
        return fabricante

    def listar_doses_disponiveis(self):
        for vacina in self.__vacinas:
            self.__tela_vacinas.mostrar_doses_disponiveis({
                "fabricante": vacina.fabricante,
                "quantidade": vacina.quantidade
            })

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
