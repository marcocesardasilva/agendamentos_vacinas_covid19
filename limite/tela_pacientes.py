
class TelaPacientes():

  def tela_opcoes(self):
    print("-------- PACIENTES ----------")
    print("Escolha a opcao")
    print("1 - Cadastrar paciente")
    print("2 - Editar paciente")
    print("3 - Consultar paciente")
    print("4 - Listar pacientes cadastrados")
    print("5 - Listar pacientes nunca agendados")
    print("6 - Listar pacientes vacinados 1ª dose")
    print("7 - Listar pacientes vacinados 2ª dose")
    print("0 - Retornar")

    opcao = int(input("Escolha a opcao: "))
    return opcao

  def pega_dados_amigo(self):
    print("-------- INCLUIR AMIGO ----------")
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    return {"nome": nome, "telefone": telefone}

  def mostra_amigo(self, dados_amigo):
    print("--------------------------------")
    print("NOME DO AMIGO: ", dados_amigo["nome"])
    print("FONE DO AMIGO: ", dados_amigo["telefone"])

