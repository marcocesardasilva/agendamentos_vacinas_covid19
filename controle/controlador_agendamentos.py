from limite.tela_agendamentos import TelaAgendamentos
from controle.controlador_enfermeiros import ControladorEnfermeiros
from controle.controlador_pacientes import ControladorPacientes
from controle.controlador_vacinas import ControladorVacinas
from entidade.agendamento import Agendamento
from entidade.enfermeiro import Enfermeiro
from entidade.vacina import Vacina
from datetime import datetime as datetime


class ControladorAgendamentos():

    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamentos = TelaAgendamentos()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_enfermeiros = self.__controlador_sistema.controlador_enfermeiros
        self.__controlador_pacientes = self.__controlador_sistema.controlador_pacientes
        self.__controlador_vacinas = self.__controlador_sistema.controlador_vacinas
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

    @property
    def agendamentos(self):
        return self.__agendamentos

    def get_agendamento(self):
        cpf_dose = self.__tela_agendamentos.selecionar_agendamento()
        for agendamento in self.__agendamentos:
            if cpf_dose["cpf"] == agendamento.paciente.cpf and cpf_dose["dose"] == agendamento.dose:
                return agendamento
    
    def consultar_agendamento(self):
        agendamento = self.get_agendamento()
        status = "Aguardando aplicação"
        if agendamento.aplicada is True:
            status = "Vacina já aplicada"
        self.__tela_agendamentos.mostrar_agendamento({
            "enfermeiro": agendamento.enfermeiro,
            "paciente": agendamento.paciente,
            "vacina": agendamento.vacina,
            "data_hora_agendamento": agendamento.data_hora_agendamento,
            "dose": agendamento.dose,
            "status": status
        })

    def editar_agendamento(self):
        agendamento = self.get_agendamento()
        dados_agendamento = self.__tela_agendamentos.pegar_dados_agendamento()
        agendamento.enfermeiro = self.__controlador_enfermeiros.get_enfermeiro()
        agendamento.paciente = self.__controlador_pacientes.get_paciente()
        agendamento.vacina = self.__controlador_vacinas.get_vacina()
        agendamento.data_hora_agendamento = datetime.strptime(
            dados_agendamento["data_hora_agendamento"],
            "%d/%m/%Y %H:%M"
        )
        agendamento.dose = dados_agendamento["dose"]

    def remover_agendamento(self):
        agendamento = self.get_agendamento()
        del(agendamento[agendamento])

    def listar_agendamentos_abertos(self):
        for agendamento in self.__agendamentos:
            if agendamento.aplicada == True:
                self.__tela_agendamentos.mostrar_lista_agendamentos({
                    "enfermeiro": agendamento.enfermeiro,
                    "paciente": agendamento.paciente,
                    "vacina": agendamento.vacina,
                    "data_hora_agendamento": agendamento.data_hora_agendamento,
                    "dose": agendamento.dose
                })

    def listar_aplicacoes_efetivadas(self):
        for agendamento in self.__agendamentos:
            if agendamento.aplicada == False:
                self.__tela_agendamentos.mostrar_lista_agendamentos({
                    "enfermeiro": agendamento.enfermeiro,
                    "paciente": agendamento.paciente,
                    "vacina": agendamento.vacina,
                    "data_hora_agendamento": agendamento.data_hora_agendamento,
                    "dose": agendamento.dose
                })

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {
            1: self.cadastrar_agendamento,
            2: self.consultar_agendamento,
            3: self.editar_agendamento,
            4: self.remover_agendamento,
            5: self.listar_agendamentos_abertos,
            6: self.listar_aplicacoes_efetivadas,
            0: self.retorna_tela_principal
        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_agendamentos.tela_opcoes()]()
