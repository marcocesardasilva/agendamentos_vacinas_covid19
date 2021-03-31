class TelaVacinas():

    def tela_opcoes(self):
        print("-------- VACINAS ----------")
        print("Escolha a opcao")
        print("1 - Cadastrar vacina")
        print("2 - Adicionar doses")
        print("3 - Subtrair doses")
        print("4 - Editar vacina")
        print("5 - Listar doses disponíveis")
        print("6 - Listar doses aplicadas")
        print("0 - Retornar")
        opcao = int(input("Escolha a opcao: "))
        return opcao

    def pegar_dados_vacina(self):
        print("-------- DADOS VACINA ----------")
        fabricante = input("Fabricante: ")
        quantidade = int(input("Quantidade: "))
        return {"fabricante": fabricante, "quantidade": quantidade}

    def pegar_quantidade(self):
        quantidade = int(input("Quantidade: "))
        return quantidade

    def selecionar_vacina(self):
        fabricante = input("Fabricante: ")
        return fabricante

    def mostrar_doses_disponiveis(self, dados_vacina):
        print("--------------------------------")
        print("Fabricante: ", dados_vacina["fabricante"])
        print("Quantidade de doses disponíveis: ", dados_vacina["quantidade"])

    def mostrar_doses_aplicadas(self):
        pass
