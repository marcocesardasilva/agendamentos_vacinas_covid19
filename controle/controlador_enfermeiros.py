from limite.tela_enfermeiros import TelaEnfermeiros
from entidade.enfermeiro import Enfermeiro


class ControladorEnfermeiros():

    def __init__(self, controlador_sistema):
        self.__enfermeiros = []
        self.__tela_enfermeiros = TelaEnfermeiros()
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def cadastrar_enfermeiro(self):
        pass

    def editar_enfermeiro(self):
        pass

    def get_enfermeiro(self):
        pass

    def remover_enfermeiro(self):
        pass

    def listar_enfermeiros(self):
        pass

    def listar_pacientes_por_enfermeiro(self):
        pass

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        pass
