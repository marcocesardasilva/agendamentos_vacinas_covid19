from limite.tela_pacientes import TelaPacientes
from entidade.paciente import Paciente


class ControladorPacientes():

    def __init__(self, controlador_sistema):
        self.__pacientes = []
        self.__tela_pacientes = TelaPacientes()
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def cadastrar_paciente(self):
        dados_paciente = self.__tela_pacientes.pega_dados_paciente()
        paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
        self.__pacientes.append(paciente)

    def editar_paciente(self):
        pass

    def get_paciente(self):
        pass

    def listar_pacientes(self):
        pass

    def listar_pacientes_nao_agendados(self):
        pass

    def listar_pacientes_primeira_dose(self):
        pass
    
    def listar_pacientes_primeira_segunda(self):
        pass

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        lista_opcoes = {1: self.cadastrar_paciente, 2: self.listar_pacientes, 0: self.retorna_tela_principal}

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_pacientes.tela_opcoes()]()
