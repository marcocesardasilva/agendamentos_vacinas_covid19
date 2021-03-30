from limite.tela_agendamentos import TelaAgendamentos
from entidade.agendamento import Agendamento
from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente
from entidade.vacina import Vacina
from datetime import datetime as datetime


class ControladorAgendamentos():

    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamentos = TelaAgendamentos()
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def cadastrar_agendamento(
        self,
        enfermeiro: Enfermeiro,
        paciente: Paciente,
        vacina: Vacina,
        data_hora_agendamento: datetime,
        dose: int
    ):
        pass

    def editar_agendamento(self):
        pass

    def get_agendamento(self):
        pass

    def remover_agendamento(self):
        pass

    def listar_agendamentos_abertos(self):
        pass

    def listar_aplicacoes_efetivadas(self):
        pass

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        pass
