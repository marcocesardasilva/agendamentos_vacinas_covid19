from entidade.pessoa import AbstractPessoa


class Enfermeiro(AbstractPessoa):
    def __init__(self, nome: str, cpf: str, matricula: int, status: str):
        super().__init__(nome, cpf)
        self.__matricula = matricula
        self.__status = status

    @property
    def matricula(self) -> int:
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status):
        if isinstance(status, str):
            self.__status = status