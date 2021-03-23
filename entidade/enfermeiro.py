
class Enfermeiro:
    def __init__(self, nome: str, cpf: str, matricula: int):
        super().__init__(nome, cpf)
        self.__nome = nome
        self.__cpf = cpf
        self.__matricula = matricula
