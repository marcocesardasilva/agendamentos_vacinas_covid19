class TelaVacinas():

    def __init__(self, controlador_vacina):
        self.__controlador_vacina = controlador_vacina

    def tela_opcoes(self):
        print("-------- VACINAS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar vacina")
        print("2 - Adicionar doses")
        print("3 - Subtrair doses")
        print("4 - Editar vacina")
        print("5 - Listar doses por fabricante")
        print("6 - Listar doses aplicadas")
        print("0 - Retornar")
        while True:
            try:
                opcao = int(input("Escolha a opcao:"))
                if 0 <= opcao <= 6:
                    return opcao
                else:
                    print("Opção escolhida inválida!")
            except ValueError:
                print("Valor digitado inválido!")

    def pegar_dados_cadastrar(self):
        print("-------- CADASTRAR VACINA ----------")
        while True:
            try:
                fabricante = input("Fabricante: ")
                if len(fabricante) == 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido para fabricante!")
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                break
            except ValueError:
                print("Valor inválido! Digite um valor válido para a quantidade.")
        return {"fabricante": fabricante, "quantidade": quantidade}
    
    def pegar_dados_editar(self):
        print("-------- EDITAR VACINA ----------")
        while True:
            try:
                fabricante = input("Fabricante: ")
                if len(fabricante) == 0:
                    raise ValueError
                break
            except ValueError:
                print("Valor inválido para fabricante!")
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                break
            except ValueError:
                print("Valor inválido! Digite um valor válido para a quantidade.")
        return {"fabricante": fabricante, "quantidade": quantidade}

    def pegar_quantidade(self):
        while True:
            try:
                quantidade = int(input("Quantidade: "))
                if quantidade < 0:
                    raise TypeError
                return quantidade
            except TypeError:
                print("Valor inválido para a quantidade. Digite um valor válido.")
        
    def selecionar_vacina(self):
        print("---- SELECIONAR VACINA ------")
        while True:
            try:
                fabricante = input("Fabricante: ")
                if len(fabricante) == 0:
                    raise ValueError
                return fabricante
            except ValueError:
                print("Valor inválido para fabricante!")

    def mostrar_doses_disponiveis(self, dados_vacina):
        print("----------------------------------------")
        print("Fabricante: {} | Quantidade: {}".format(dados_vacina["fabricante"],dados_vacina["quantidade"]))

    def mostrar_doses_aplicadas(self, dados_vacina):
        for fabricante,quantidade in dados_vacina.items():
            print("Fabricante: {} | Quantidade: {}" .format(fabricante, quantidade))

    def vacina_ja_cadastrada(self):
        print("Fabricante digitado já existe no sistema.")
    
    def vacina_cadastrada(self):
        print("Vacina cadastrada com sucesso!")

    def quantidade_insuficiente(self, quantidade):
        print("Quantidade disponível insuficiente. Seu estoque é de {} doses.".format(quantidade))

    def vacina_nao_cadastrada(self):
        print("Vacina não cadastrada.")
