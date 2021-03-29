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
