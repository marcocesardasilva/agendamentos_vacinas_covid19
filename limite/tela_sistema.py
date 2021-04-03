class TelaSistema:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema

    def tela_opcoes(self):
        print("-------- POSTO DE VACINAÇÃO --------")
        print("Escolha uma opção da lista:")
        print("1 - Enfermeiros")
        print("2 - Pacientes")
        print("3 - Vacinas")
        print("4 - Agendamentos")
        print("0 - Finalizar sistema")
        while True:
            try:
                opcao = int(input("Escolha sua opção:"))
                if 0 <= opcao <= 4:
                    return opcao
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")
