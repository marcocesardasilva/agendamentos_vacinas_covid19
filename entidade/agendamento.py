from entidade.vacina import Vacina
from entidade.enfermeiro import Enfermeiro
from entidade.paciente import Paciente
from datetime import datetime as datetime


class Agendamento:
    def __init__(
        self,
        enfermeiro: Enfermeiro,
        paciente: Paciente,
        vacina: Vacina,
        data_hora_agendamento: datetime,
        dose: int
    ):
        self.__enfermeiro = enfermeiro
        self.__paciente = paciente
        self.__vacina = vacina
        self.__data_hora_agendamento = data_hora_agendamento
        self.__dose = dose
        self.__aplicada = False

    @property
    def enfermeiro(self) -> Enfermeiro:
        return self.__enfermeiro

    @enfermeiro.setter
    def enfermeiro(self, enfermeiro):
        if isinstance(enfermeiro, Enfermeiro):
            self.__enfermeiro = enfermeiro

    @property
    def paciente(self) -> Paciente:
        return self.__paciente

    @paciente.setter
    def paciente(self, paciente):
        if isinstance(paciente, Paciente):
            self.__paciente = paciente

    @property
    def vacina(self) -> Vacina:
        return self.__vacina

    @vacina.setter
    def vacina(self, vacina):
        if isinstance(vacina, Vacina):
            self.__vacina = vacina

    @property
    def data_hora_agendamento(self) -> datetime:
        return self.__data_hora_agendamento

    @data_hora_agendamento.setter
    def data_hora_agendamento(self, data_hora_agendamento):
        if isinstance(data_hora_agendamento, datetime):
            self.__data_hora_agendamento = data_hora_agendamento

    @property
    def dose(self) -> int:
        return self.__dose

    @dose.setter
    def dose(self, dose):
        if isinstance(dose, int):
            self.__dose = dose

    @property
    def aplicada(self) -> bool:
        return self.__aplicada

    @aplicada.setter
    def aplicada(self, aplicada):
        if isinstance(aplicada, bool):
            self.__aplicada = aplicada
