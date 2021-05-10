from limite.tela_enfermeiros import TelaEnfermeiros
from entidade.enfermeiro import Enfermeiro
from persistencia.enfermeiroDAO import EnfermeiroDAO
from datetime import datetime as datetime


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
            if dados_enfermeiro is None:
                break
            for enfermeiro in self.__dao.get_all():
                if enfermeiro.matricula == dados_enfermeiro["matricula"]:
                    self.__tela_enfermeiros.mensagem('Enfermeiro ja cadastrado com esta matrícula')
                    return None
                elif enfermeiro.cpf == dados_enfermeiro["cpf"]:
                    self.__tela_enfermeiros.mensagem('Enfermeiro ja cadastrado com este cpf')
                    return None
            try:
                nome = dados_enfermeiro["nome"].upper()
                if nome.replace(' ', '').isalpha():
                    nome_ok = nome
                else:
                    self.__tela_enfermeiros.mensagem(f'O nome {nome} é inválido!')
                    break
            except (ValueError, TypeError):
                self.__tela_enfermeiros.mensagem('Houve problemas com o tipo de dado digitado')
            try:
                cpf = dados_enfermeiro["cpf"].replace(' ','')
                if cpf.isnumeric() and len(cpf) == 11:
                    cpf_ok = cpf
                else:
                    self.__tela_enfermeiros.mensagem(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
                    break
            except (ValueError, TypeError):
                self.__tela_enfermeiros.mensagem('Houve problemas com o tipo de dado digitado')
            try:
                matricula = dados_enfermeiro["matricula"].replace(' ','')
                if matricula.isnumeric() and len(matricula) == 4:
                    matricula_ok = matricula
                else:
                    self.__tela_enfermeiros.mensagem(f'A matrícula {matricula} é inválida!\nDigite uma matrícula com 4 dígitos')
                    break
            except (ValueError, TypeError):
                self.__tela_enfermeiros.mensagem('Houve problemas com o tipo de dado digitado')
            enfermeiro = Enfermeiro(nome_ok,
                                    cpf_ok,
                                    matricula_ok,
                                    dados_enfermeiro["status"])
            self.__tela_enfermeiros.mensagem("Enfermeiro cadastrado!")
            self.__dao.add(enfermeiro)
            break

    def editar_enfermeiro(self):
        enfermeiro_editar = self.get_enfermeiro()
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            elif enfermeiro_editar is None:
                raise Exception
            dados_editar = self.__tela_enfermeiros.pegar_dados_enfermeiro()
            for enfermeiro in self.__dao.get_all():
                if enfermeiro.matricula == dados_editar["matricula"]:
                    self.__tela_enfermeiros.matricula_ja_cadastrada(dados_editar["matricula"])
                    raise Exception
            if enfermeiro_editar is not None:
                try:
                    nome = dados_editar["nome"].upper()
                    if nome.replace(' ', '').isalpha():
                        nome_ok = nome
                    else:
                        self.__tela_enfermeiros.mensagem(f'O nome {nome} é inválido!')
                except (ValueError, TypeError):
                    self.__tela_enfermeiros.mensagem('Houve problemas com o tipo de dado digitado')
                try:
                    cpf = dados_editar["cpf"].replace(' ', '')
                    if cpf.isnumeric() and len(cpf) == 11:
                        cpf_ok = cpf
                    else:
                        self.__tela_enfermeiros.mensagem(f'O cpf {cpf} é inválido!\nDigite um cpf com 11 dígitos')
                except (ValueError, TypeError):
                    self.__tela_enfermeiros.mensagem('Houve problemas com o tipo de dado digitado')
                enfermeiro_editar.cpf = cpf_ok
                enfermeiro_editar.nome = nome_ok
                enfermeiro_editar.status = dados_editar["status"]
                self.__dao.add(enfermeiro_editar)
        except Exception:
            pass

    def get_enfermeiro(self):
        if len(self.__dao.get_all()) == 0:
            self.__tela_enfermeiros.nenhum_enfermeiro()
            return None
        else:
            matricula = self.selecionar_lista_enfermeiros()
            if matricula is None:
                return None
            if self.__dao.get(matricula):
                return self.__dao.get(matricula)
            else:
                self.__tela_enfermeiros.enfermeiro_nao_cadastrado()

    def enfermeiro_inativo(self):
        self.__tela_enfermeiros.mensagem('Enfermeiro inativo')

    def alterar_status_enfermeiro(self):
        enfermeiro = self.get_enfermeiro()
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            status = self.__tela_enfermeiros.status_enfermeiro(enfermeiro.matricula)
            enfermeiro.status = status
            self.__dao.add(enfermeiro)
        except Exception:
            pass

    def selecionar_lista_enfermeiros(self):
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            matriz = [['        Nome        ', 'CPF', 'Matrícula', 'Status']]
            for enfermeiro in self.__dao.get_all():
                linha = [enfermeiro.nome, enfermeiro.cpf, enfermeiro.matricula, enfermeiro.status]
                matriz.append(linha)
            enfermeiro_selecionado = self.__tela_enfermeiros.selecionar_enfermeiro_tabela(matriz, 'Selecionar enfermeiros')
            if enfermeiro_selecionado:
                return matriz[enfermeiro_selecionado[0]+1][2]
        except Exception:
            self.__tela_enfermeiros.mensagem('Não há enfermeiros cadastrados até o momento.')

    def listar_enfermeiros(self):
        try:
            if len(self.__dao.get_all()) == 0:
                raise Exception
            matriz = [['        Nome        ', 'CPF', 'Matrícula', 'Status']]
            for enfermeiro in self.__dao.get_all():
                linha = [enfermeiro.nome, enfermeiro.cpf, enfermeiro.matricula, enfermeiro.status]
                matriz.append(linha)
            self.__tela_enfermeiros.mostrar_enfermeiro_tabela(matriz, 'Enfermeiros')
        except Exception:
            self.__tela_enfermeiros.mensagem('Não há enfermeiros cadastrados até o momento.')

    def listar_pacientes_por_enfermeiro(self):
        self.__controlador_pacientes = self.__controlador_sistema.controlador_pacientes
        self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        matriz = []
        linha = ['        Nome        ', '    CPF    ', 'Idade']
        matriz.append(linha)
        try:
            if len(self.__controlador_agendamentos.agendamentos) == 0:
                raise IndexError
            enfermeiro_listar = self.get_enfermeiro()
            dados_enfermeiro = {"nome": enfermeiro_listar.nome, "matricula": enfermeiro_listar.matricula}
            if enfermeiro_listar is None:
                raise TypeError
            for agendamento in self.__controlador_agendamentos.agendamentos:
                if agendamento.enfermeiro.matricula == enfermeiro_listar.matricula:
                    linha = [agendamento.paciente.nome, agendamento.paciente.cpf]
                    idade_dias = datetime.today().date() - agendamento.paciente.data_nascimento
                    idade = idade_dias.days // 365.24231481481481481481481481481481
                    linha.append(idade)
                    matriz.append(linha)
            self.__tela_enfermeiros.mostrar_pacientes_por_enfermeiro(dados_enfermeiro, matriz)
        except IndexError:
            self.__tela_enfermeiros.nenhum_agendamento()
        except TypeError:
            pass

    def remover_enfermeiro(self):
        enfermeiro = self.get_enfermeiro()
        if enfermeiro is not None:
            self.__dao.remove(enfermeiro.matricula)
        #ESTÁ COM ERRO AQUI, NÃO ESTÁ REMOVENDO, VOLTEI O CÓDIGO PARA VERIFICARMOS.
        # self.__controlador_agendamentos = self.__controlador_sistema.controlador_agendamentos
        # enfermeiro = self.get_enfermeiro()
        # for agendamento in self.__controlador_agendamentos.agendamentos:
        #     if agendamento.enfermeiro == enfermeiro:
        #         return None
        # if enfermeiro is not None:
        #     self.__dao.remove(enfermeiro.matricula)

    def retorna_tela_principal(self):
        self.__mantem_tela_aberta = False

    def abre_tela(self):
        self.__mantem_tela_aberta = True
        lista_opcoes = {1: self.cadastrar_enfermeiro,
                        2: self.editar_enfermeiro,
                        3: self.alterar_status_enfermeiro,
                        4: self.listar_enfermeiros,
                        5: self.listar_pacientes_por_enfermeiro,
                        6: self.remover_enfermeiro,
                        0: self.retorna_tela_principal
                        }

        while self.__mantem_tela_aberta:
            lista_opcoes[self.__tela_enfermeiros.tela_opcoes()]()
