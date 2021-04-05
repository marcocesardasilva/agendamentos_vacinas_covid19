from limite.tela_agendamentos import TelaAgendamentos
from entidade.agendamento import Agendamento
from datetime import datetime


class ControladorAgendamentos():

    def __init__(self, controlador_sistema):
        self.__agendamentos = []
        self.__tela_agendamentos = TelaAgendamentos(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_enfermeiros = self.__controlador_sistema.controlador_enfermeiros
        self.__controlador_pacientes = self.__controlador_sistema.controlador_pacientes
        self.__controlador_vacinas = self.__controlador_sistema.controlador_vacinas
        self.__mantem_tela_aberta = True

    def cadastrar_agendamento(self):
        dados_agendamento = self.__tela_agendamentos.pegar_dados_cadastrar()
        while True:
            paciente = self.__controlador_pacientes.get_paciente()
            if paciente is None:
                break
            if dados_agendamento["dose"] == 1:
                dose1 = False
                for agendamento in self.__agendamentos:
                    if agendamento.paciente == paciente and agendamento.dose == 1:
                        dose1 = True
                if dose1 == True:
                    self.__tela_agendamentos.ja_castrado_primeira_dose()
                    break
            if dados_agendamento["dose"] == 2:
                dose1 = False
                for agendamento in self.__agendamentos:
                    if agendamento.paciente == paciente and agendamento.dose == 1:
                        dose1 = True
                        diferenca_dias = dados_agendamento["data"] - agendamento.data
                        if diferenca_dias.days <= 20:
                            self.__tela_agendamentos.data_recente_primeira_dose()
                            break
                if dose1 == False:
                    self.__tela_agendamentos.nao_castrado_primeira_dose()
                    break
                dose2 = False
                for agendamento in self.__agendamentos:
                    if agendamento.paciente == paciente and agendamento.dose == 2:
                        dose2 = True
                if dose2 == True:
                    self.__tela_agendamentos.ja_castrado_segunda_dose()
                    break
            enfermeiro = self.__controlador_enfermeiros.get_enfermeiro()
            if enfermeiro is None:
                break
            if enfermeiro.status == "Inativo":
                self.__controlador_enfermeiros.enfermeiro_inativo()
                break
            vacina = self.__controlador_vacinas.get_vacina()
            if vacina is None:
                break
            if vacina.quantidade < 1:
                self.__controlador_vacinas.chamar_doses_insuficiente()
                break
            vacina.subtrai_quantidade(1)
            
            agendamento = Agendamento(
                enfermeiro,
                paciente,
                vacina,
                dados_agendamento["data"],
                dados_agendamento["horario"],
                dados_agendamento["dose"]
            )
            self.__agendamentos.append(agendamento)
            self.__tela_agendamentos.agendamento_cadastrado()
            break

    @property
    def agendamentos(self):
        return self.__agendamentos

    def get_agendamento(self):
        dose = self.__tela_agendamentos.selecionar_agendamento()
        paciente = self.__controlador_pacientes.get_paciente()
        if paciente is None:
            return None
        if len(self.__agendamentos) == 0:
            self.__tela_agendamentos.agendamento_nao_cadastrado()
            return None
        else:
            for agendamento in self.__agendamentos:
                if dose == agendamento.dose and paciente.cpf == agendamento.paciente.cpf:
                    return agendamento
        self.__tela_agendamentos.agendamento_nao_cadastrado()
        return None


    
    def consultar_agendamento(self):
        agendamento = self.get_agendamento()
        if agendamento is None:
            return None
        status = "Aguardando aplicação"
        if agendamento.aplicada is True:
            status = "Vacina já aplicada"
        self.__tela_agendamentos.mostrar_agendamento({
            "enfermeiro": agendamento.enfermeiro.nome,
            "paciente": agendamento.paciente.nome,
            "vacina": agendamento.vacina.fabricante,
            "data": agendamento.data,
            "horario": agendamento.horario,
            "dose": agendamento.dose,
            "status": status
        })

    def editar_agendamento(self):
        agendamento = self.get_agendamento()
        if agendamento is None:
            return None
        dados_agendamento = self.__tela_agendamentos.pegar_dados_editar()
        while True:
            paciente = self.__controlador_pacientes.get_paciente()
            if paciente is None:
                break
            if dados_agendamento["dose"] == 1:
                dose1 = False
                for agendamento in self.__agendamentos:
                    if agendamento.paciente == paciente and agendamento.dose == 1:
                        dose1 = True
                if dose1 == True:
                    self.__tela_agendamentos.ja_castrado_primeira_dose()
                    break
            if dados_agendamento["dose"] == 2:
                dose1 = False
                for agendamento in self.__agendamentos:
                    if agendamento.paciente == paciente and agendamento.dose == 1:
                        dose1 = True
                        diferenca_dias = dados_agendamento["data"] - agendamento.data
                        if diferenca_dias.days <= 20:
                            self.__tela_agendamentos.data_recente_primeira_dose()
                            break
                if dose1 == False:
                    self.__tela_agendamentos.nao_castrado_primeira_dose()
                    break
                dose2 = False
                for agendamento in self.__agendamentos:
                    if agendamento.paciente == paciente and agendamento.dose == 2:
                        dose2 = True
                if dose2 == True:
                    self.__tela_agendamentos.ja_castrado_segunda_dose()
                    break
            enfermeiro = self.__controlador_enfermeiros.get_enfermeiro()
            if enfermeiro is None:
                break
            if enfermeiro.status == "Inativo":
                self.__controlador_enfermeiros.enfermeiro_inativo()
                break
            vacina = self.__controlador_vacinas.get_vacina()
            if vacina is None:
                break
            if vacina.quantidade < 1:
                self.__controlador_vacinas.chamar_doses_insuficiente()
                break
        agendamento.enfermeiro = agendamento
        agendamento.paciente = paciente
        agendamento.vacina = vacina
        agendamento.data = dados_agendamento["data"]
        agendamento.horario = dados_agendamento["horario"]
        agendamento.dose = dados_agendamento["dose"]
        agendamento.aplicada = dados_agendamento["aplicada"]
        self.__tela_agendamentos.agendamento_editado()

    def aplicar_vacina(self):
        agendamento = self.get_agendamento()
        if agendamento is None:
            return None
        agendamento.aplicada = True
        self.__tela_agendamentos.vacina_aplicada()

    def remover_agendamento(self):
        agendamento = self.get_agendamento()
        if agendamento is None:
            return None
        else:
            agendamento.vacina.adiciona_quantidade(1)
            for i in range(len(self.__agendamentos)):
                if agendamento == self.__agendamentos[i]:
                    del(self.__agendamentos[i])
            self.__tela_agendamentos.agendamento_removido()

    def listar_agendamentos_abertos(self):
        if len(self.__agendamentos) == 0:
            self.__tela_agendamentos.agendamento_aberto_nao_cadastrado()
            return None
        encontrado = False
        contador = 0
        while encontrado is False and contador < len(self.__agendamentos):
            for agendamento in self.__agendamentos:
                if agendamento.aplicada == True:
                    contador += 1
                else:
                    encontrado = True
        if encontrado == False:
            self.__tela_agendamentos.agendamento_aberto_nao_cadastrado()
        else:    
            for agendamento in self.__agendamentos:
                if agendamento.aplicada == False:
                    self.__tela_agendamentos.mostrar_lista_agendamentos({
                        "enfermeiro": agendamento.enfermeiro.nome,
                        "paciente": agendamento.paciente.nome,
                        "vacina": agendamento.vacina.fabricante,
                        "data": agendamento.data,
                        "horario": agendamento.horario,
                        "dose": agendamento.dose
                    })

    def listar_aplicacoes_efetivadas(self):
        if len(self.__agendamentos) == 0:
            self.__tela_agendamentos.agendamento_efetivado_nao_cadastrado()
            return None
        encontrado = False
        contador = 0
        while encontrado is False and contador < len(self.__agendamentos):
            for agendamento in self.__agendamentos:
                if agendamento.aplicada == False:
                    contador += 1
                else:
                    encontrado = True
        if encontrado == False:
            self.__tela_agendamentos.agendamento_efetivado_nao_cadastrado()
        else:    
            for agendamento in self.__agendamentos:
                if agendamento.aplicada == True:
                    self.__tela_agendamentos.mostrar_lista_agendamentos({
                        "enfermeiro": agendamento.enfermeiro.nome,
                        "paciente": agendamento.paciente.nome,
                        "vacina": agendamento.vacina.fabricante,
                        "data": agendamento.data,
                        "horario": agendamento.horario,
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
            4: self.aplicar_vacina,
            5: self.remover_agendamento,
            6: self.listar_agendamentos_abertos,
            7: self.listar_aplicacoes_efetivadas,
            0: self.retorna_tela_principal
        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_agendamentos.tela_opcoes()]()
