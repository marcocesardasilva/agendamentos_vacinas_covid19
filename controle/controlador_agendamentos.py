from limite.tela_agendamentos import TelaAgendamentos
from controle.controlador_enfermeiros import ControladorEnfermeiros
from controle.controlador_pacientes import ControladorPacientes
from controle.controlador_vacinas import ControladorVacinas
from datetime import datetime as datetime


class ControladorAgendamentos():

    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamentos = TelaAgendamentos()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_enfermeiros = ControladorEnfermeiros()
        self.__controlador_pacientes = ControladorPacientes()
        self.__controlador_vacinas = ControladorVacinas()
        self.__mantem_tela_aberta = True

    def cadastrar_agendamento(self):
        dados_agendamento = self.__tela_agendamentos.pegar_dados_agendamento()
        enfermeiro = self.__controlador_enfermeiros.get_enfermeiro()
        paciente = self.__controlador_pacientes.get_paciente()
        vacina = self.__controlador_vacinas.get_vacina()
        data_hora_agendamento = datetime.strptime(
            dados_agendamento["data_hora_agendamento"],
            "%d/%m/%Y %H:%M"
        )

        agendamento = Agendamento(
            enfermeiro,
            paciente,
            vacina,
            data_hora_agendamento,
            dados_agendamento["dose"]
        )
        self.__agendamentos.append(agendamento)

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
        lista_opcoes = {
            1: self.cadastrar_agendamento,
            2: self.editar_agendamento,
            3: self.get_agendamento,
            4: self.remover_agendamento,
            5: self.listar_agendamentos_abertos,
            6: self.listar_aplicacoes_efetivadas,
            0: self.retorna_tela_principal
        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_agendamentos.tela_opcoes()]()
