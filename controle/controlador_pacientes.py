from limite.tela_pacientes import TelaPacientes
from entidade.paciente import Paciente


class ControladorPacientes():

    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_pacientes = TelaPacientes()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_agendamentos = None
        self.__mantem_tela_aberta = True

    def cadastrar_paciente(self):
        dados_paciente = self.__tela_pacientes.pega_dados_paciente()
        paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
        self.__pacientes.append(paciente)

    def editar_paciente(self):
        paciente_editar = self.get_paciente()
        dados_editar = self.__tela_pacientes.pega_dados_paciente_edicao()
        for paciente in self.__pacientes:
            if paciente_editar == paciente:
                paciente.nome = dados_editar["nome"]
                paciente.data_nascimento = dados_editar["data_nascimento"]

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
        cpf = self.__tela_pacientes.selecionar_paciente()
        for paciente in self.__pacientes:
            if cpf == paciente.cpf:
                return paciente

    def listar_pacientes(self):
        for paciente in self.__pacientes:
            self.__tela_pacientes.mostrar_paciente(
                {"nome": paciente.nome,
                 "cpf": paciente.cpf,
                 "data_nascimento": paciente.data_nascimento}
            )

    def listar_pacientes_nao_agendados(self):
        # for paciente in self.__pacientes:
        #     if paciente not in agendamentos:
        #         self.__tela_pacientes.mostrar_paciente()
        pass

    def listar_pacientes_primeira_dose(self):
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        for agendamento in self.__controlador_agendamentos.agendamentos:
            print(agendamento.dose)

    
    def listar_pacientes_primeira_segunda(self):
        pass

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
                        7: self.listar_pacientes_primeira_segunda,
                        0: self.retorna_tela_principal}

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_pacientes.tela_opcoes()]()
