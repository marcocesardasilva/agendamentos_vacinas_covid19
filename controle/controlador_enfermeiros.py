from limite.tela_enfermeiros import TelaEnfermeiros
from entidade.enfermeiro import Enfermeiro
from persistencia.enfermeiroDAO import EnfermeiroDAO


class ControladorEnfermeiros():

    def __init__(self, controlador_sistema):
        self.__dao = EnfermeiroDAO()
        self.__tela_enfermeiros = TelaEnfermeiros(self)
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pacientes = None
        self.__controlador_agendamentos = None
        self.__mantem_tela_aberta = True

    def cadastrar_enfermeiro(self):
        while True:
            dados_enfermeiro = self.__tela_enfermeiros.pegar_dados_enfermeiro()
            for enfermeiro in self.__dao.get_all():
                if enfermeiro.matricula == dados_enfermeiro["matricula"]:
                    self.__tela_enfermeiros.matricula_ja_cadastrada(dados_enfermeiro["matricula"])
                    return None
                elif enfermeiro.cpf == dados_enfermeiro["cpf"]:
                    self.__tela_enfermeiros.cpf_ja_cadastrado(dados_enfermeiro["cpf"])
                    return None
            enfermeiro = Enfermeiro(dados_enfermeiro["nome"],
                                    dados_enfermeiro["cpf"],
                                    dados_enfermeiro["matricula"],
                                    dados_enfermeiro["status"])
            self.__dao.add(enfermeiro)
            break

    def editar_enfermeiro(self):
        enfermeiro_editar = self.get_enfermeiro()
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            elif enfermeiro_editar is None:
                raise Exception
            dados_editar = self.__tela_enfermeiros.pegar_dados_enfermeiro_edicao()
            for enfermeiro in self.__dao.get_all():
                if enfermeiro.matricula == dados_editar["matricula"]:
                    self.__tela_enfermeiros.matricula_ja_cadastrada(dados_editar["matricula"])
                    raise Exception
            for enfermeiro in self.__dao.get_all():
                if enfermeiro == enfermeiro_editar:
                    enfermeiro.nome = dados_editar['nome']
                    enfermeiro.matricula = dados_editar['matricula']
        except Exception:
            pass

    def consultar_enfermeiro(self):
        try:
            enfermeiro = self.get_enfermeiro()
            if len(self.__dao.get_all()) == 0:
                raise Exception
            self.__tela_enfermeiros.mostrar_enfermeiro(
                {"nome": enfermeiro.nome,
                 "cpf": enfermeiro.cpf,
                 "matricula": enfermeiro.matricula,
                 "status": enfermeiro.status}
            )
        except Exception:
            pass

    def get_enfermeiro(self):
        matricula = self.__tela_enfermeiros.selecionar_enfermeiro()
        if len(self.__dao.get_all()) == 0:
            self.__tela_enfermeiros.enfermeiro_nao_cadastrado()
            return None
        else:
            for enfermeiro in self.__dao.get_all():
                if matricula == enfermeiro.matricula:
                    return enfermeiro
        self.__tela_enfermeiros.enfermeiro_nao_cadastrado()
        return None

    def enfermeiro_inativo(self):
        self.__tela_enfermeiros.enfermeiro_inativo()

    def alterar_status_enfermeiro(self):
        enfermeiro = self.get_enfermeiro()
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            status = self.__tela_enfermeiros.status_enfermeiro(enfermeiro.matricula)
            enfermeiro.status = status
        except Exception:
            pass

    def listar_enfermeiros(self):
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            for enfermeiro in self.__dao.get_all():
                self.__tela_enfermeiros.mostrar_enfermeiro(
                    {"nome": enfermeiro.nome,
                     "cpf": enfermeiro.cpf,
                     "matricula": enfermeiro.matricula,
                     "status": enfermeiro.status}
                )
        except Exception:
            self.__tela_enfermeiros.nenhum_enfermeiro()

    def listar_pacientes_por_enfermeiro(self):
        self.__controlador_pacientes = self.__controlador_sistema.controlador_pacientes
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                raise IndexError
            enfermeiro_listar = self.get_enfermeiro()
            if enfermeiro_listar is None:
                raise TypeError
            for enfermeiro in self.__dao.get_all():
                #Verificar isso
                if enfermeiro.cpf == enfermeiro_listar.cpf:
                    self.__tela_enfermeiros.mostrar_enfermeiro(
                        {"nome": enfermeiro.nome,
                         "cpf": enfermeiro.cpf,
                         "matricula": enfermeiro.matricula,
                         "status": enfermeiro.status}
                        )
            for agendamento in self.__controlador_agendamentos.agendamentos:
                if agendamento.enfermeiro.matricula == enfermeiro_listar.matricula:
                    self.__tela_enfermeiros.mostrar_pacientes_por_enfermeiro(
                        {"nome": agendamento.paciente.nome,
                         "cpf": agendamento.paciente.cpf,
                         "data_nascimento": agendamento.paciente.data_nascimento}
                        )
            self.__tela_enfermeiros.linha()
        except IndexError:
            self.__tela_enfermeiros.nenhum_agendamento()
        except TypeError:
            pass


    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_enfermeiro,
                        2: self.editar_enfermeiro,
                        3: self.consultar_enfermeiro,
                        4: self.alterar_status_enfermeiro,
                        5: self.listar_enfermeiros,
                        6: self.listar_pacientes_por_enfermeiro,
                        0: self.retorna_tela_principal
                        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_enfermeiros.tela_opcoes()]()
