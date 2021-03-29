from limite.tela_pacientes import TelaPacientes
from entidade.paciente import Paciente

class ControladorPacientes():

    def __init__(self, controlador_sistema):

        self.__pacientes = []
        self.__tela_pacientes = TelaPacientes()
        self.__controlador_sistema = controlador_sistema
        self.__mantem_tela_aberta = True

    def incluir_paciente(self):
        dados_paciente = self.__tela_pacientes.pega_dados_paciente()
        paciente = Paciente(dados_paciente["nome"], dados_paciente["cpf"], dados_paciente["data_nascimento"])
        self.__pacientes.append(paciente)

    def listar_pacientes(self):
        for paciente in self.__pacientes:
            self.__tela_pacientes.mostrar_paciente({"nome": nome, "cpf": cpf, "data de nascimento": data_nascimento})

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_paciente, 2: self.listar_pacientes, 0: self.retorna_tela_principal}

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_pacientes.tela_opcoes()]()


