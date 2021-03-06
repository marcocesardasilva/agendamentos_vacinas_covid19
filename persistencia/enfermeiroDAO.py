from persistencia.dao import DAO
from entidade.enfermeiro import Enfermeiro


class EnfermeiroDAO(DAO):
    def __init__(self):
        super().__init__('dados/enfermeiros.pkl')

    def add(self, enfermeiro: Enfermeiro):
        if (isinstance(enfermeiro.matricula, str)) and (enfermeiro is not None) \
                and isinstance(enfermeiro, Enfermeiro):
            super().add(enfermeiro.matricula, enfermeiro)
    
    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
