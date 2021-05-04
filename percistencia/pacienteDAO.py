from DAO import DAO
from entidade.paciente import Paciente


class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('paciente.pkl')

    def add(self, paciente: Paciente):
        if (isinstance(paciente.cpf, str)) and (paciente is not None) \
                and isinstance(paciente, Paciente):
            super().add(paciente.codigo, paciente)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
