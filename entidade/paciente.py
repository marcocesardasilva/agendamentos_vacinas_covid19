from datetime import date

class Paciente:
  def __init__(self, nome: str, cpf: str, data_nascimento: date):
    super().__init__(nome, cpf)
    self.__nome = nome
    self.__cpf = cpf
    self.__data_nascimento = data_nascimento
  

