from limite.tela_pacientes import TelaPacientes
from entidade.paciente import Paciente
from controle.controlador_agendamentos import ControladorAgendamentos
from datetime import datetime as datetime
from math import trunc


class ControladorPacientes():

    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_pacientes = TelaPacientes(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_agendamentos = None
        self.__mantem_tela_aberta = True

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    def pacientes(self):
        return self.__pacientes

    def cadastrar_paciente(self):
        while True:
            dados_paciente = self.__tela_pacientes.pega_dados_paciente()
            if len(self.__pacientes) == 0:
                paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
                self.__pacientes.append(paciente)
                break
            else:
                for paciente in self.__pacientes:
                    if dados_paciente["cpf"] == paciente.cpf:
                        self.__tela_pacientes.cpf_ja_cadastrado(dados_paciente['cpf'])
                        return None
                paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
                self.__pacientes.append(paciente)
                self.__tela_pacientes.sucesso(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
                break

    def editar_paciente(self):
        paciente_editar = self.get_paciente()
        #rever
        if paciente_editar is None:
            return None
        dados_editar = self.__tela_pacientes.pega_dados_paciente_edicao()
        for paciente in self.__pacientes:
            if paciente_editar == paciente:
                paciente.nome = dados_editar["nome"]
                paciente.data_nascimento = dados_editar["data_nascimento"]
                self.__tela_pacientes.sucesso(dados_editar["nome"], dados_editar["data_nascimento"])

    def consultar_paciente(self):
        paciente_consultar = self.get_paciente()
        for paciente in self.__pacientes:
            if paciente_consultar == paciente:
                self.__tela_pacientes.mostrar_paciente(
                    {"nome": paciente.nome,
                     "cpf": paciente.cpf,
                     "data_nascimento": paciente.data_nascimento}
                    )

    def get_paciente(self):
        if len(self.__pacientes) == 0:
            self.__tela_pacientes.nenhum_paciente()
            return None
        else:
            cpf = self.__tela_pacientes.selecionar_paciente()
            for paciente in self.__pacientes:
                if cpf == paciente.cpf:
                    return paciente
        self.__tela_pacientes.cpf_nao_cadastrado(cpf)
        return None

    def listar_pacientes(self):
        try:
            for paciente in self.__pacientes:
                self.__tela_pacientes.mostrar_paciente(
                    {"nome": paciente.nome,
                     "cpf": paciente.cpf,
                     "data_nascimento": paciente.data_nascimento}
                )
        except:
            self.__tela_pacientes.nenhum_paciente()

    def listar_pacientes_nao_agendados(self):
        pacientes_agendados = []
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                self.__tela_pacientes.nenhum_agendamento()
            for agendamento in self.__controlador_agendamentos.agendamentos:
                for paciente in self.__pacientes:
                    if agendamento.paciente == paciente:
                        pacientes_agendados.append(paciente)
            for paciente in self.__pacientes:
                if paciente not in pacientes_agendados:
                    self.__tela_pacientes.mostrar_paciente(
                        {"nome": paciente.nome,
                        "cpf": paciente.cpf,
                        "data_nascimento": paciente.data_nascimento
                        })
        except Exception:
            self.__tela_pacientes.nenhum_agendamento()

    def pacientes_aguardando_vacina(self):
        pacientes_com_agendamento = 0
        pacientes_total = len(self.__pacientes)
        pacientes_sem_agendamento = 0
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__pacientes) == 0:
                return 0
            for agendamento in self.__controlador_agendamentos.agendamentos:
                for paciente in self.__pacientes:
                    if agendamento.paciente == paciente and agendamento.dose == 1:
                        pacientes_com_agendamento += 1
            pacientes_sem_agendamento = pacientes_total - pacientes_com_agendamento
        except:
            self.__tela_pacientes.nenhum_agendamento()
        return pacientes_sem_agendamento

    def listar_pacientes_primeira_dose(self):
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                raise Exception
            for agendamento in self.__controlador_agendamentos.agendamentos:
                if agendamento.dose == 1:
                    if agendamento.aplicada:
                        self.__tela_pacientes.mostrar_paciente(
                            {"nome": agendamento.paciente.nome,
                             "cpf": agendamento.paciente.cpf,
                             "data_nascimento": agendamento.paciente.data_nascimento
                            }
                        )
        except Exception:
            self.__tela_pacientes.nenhum_agendamento()
    
    def listar_pacientes_segunda_dose(self):
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                raise Exception
            for agendamento in self.__controlador_agendamentos.agendamentos:
                if agendamento.dose == 2:
                    if agendamento.aplicada:
                        self.__tela_pacientes.mostrar_paciente(
                            {"nome": agendamento.paciente.nome,
                             "cpf": agendamento.paciente.cpf,
                             "data_nascimento": agendamento.paciente.data_nascimento
                            }
                        )
        except Exception:
            self.__tela_pacientes.nenhum_agendamento()

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_paciente,
                        2: self.editar_paciente,
                        3: self.consultar_paciente,
                        4: self.listar_pacientes,
                        5: self.listar_pacientes_nao_agendados,
                        6: self.listar_pacientes_primeira_dose,
                        7: self.listar_pacientes_segunda_dose,
                        0: self.retorna_tela_principal}

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_pacientes.tela_opcoes()]()
