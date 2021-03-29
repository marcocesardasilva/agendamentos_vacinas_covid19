from entidade.pessoa import AbstractPessoa


class Enfermeiro(AbstractPessoa):
    def __init__(self, nome: str, cpf: str, matricula: int):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self) -> int:
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula
