class TelaSistema:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        print("-------- SisPostoVacinas --------")
        print("Escolha sua opcao")
        print("1 - Agendamentos")
        print("2 - Vacinas")
        print("3 - Enfermeiros")
        print("4 - Pacientes")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
