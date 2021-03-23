from limite.tela_pacientes import TelaPacientes
from entidade.paciente import Paciente

class ControladorPacientes():

  def __init__(self, controlador_sistema):

    self.__amigos = []
    self.__tela_amigo = TelaAmigo()
    self.__controlador_sistema = controlador_sistema
    self.__mantem_tela_aberta = True

  def incluir_amigo(self):
    dados_amigo = self.__tela_amigo.pega_dados_amigo()
    amigo = Amigo(dados_amigo["nome"], dados_amigo["telefone"])
    self.__amigos.append(amigo)

  def altera_amigo(self):
    pass

  def exclui_amigo(self):
    pass

  def lista_amigos(self):
    for amigo in self.__amigos:
      self.__tela_amigo.mostra_amigo({"nome": amigo.nome, "telefone": amigo.telefone})
  
  def retorna_tela_principal(self):
    self.__mantem_tela_aberta = False


  def abre_tela(self):
    lista_opcoes = {1: self.incluir_amigo, 2: self.altera_amigo, 3: self.lista_amigos, 4: self.exclui_amigo, 0: self.retorna_tela_principal}

    while self.__mantem_tela_aberta:
      lista_opcoes[self.__tela_amigo.tela_opcoes()]()


