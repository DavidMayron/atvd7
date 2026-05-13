# atividade07
# Sistema de Cinema

# Função do menu
def menu():
    print(" Bem-vindo ao Cinema!")
    nome = input("Digite seu nome: ")
    return nome


# Função para escolher filme
def escolher_filme():
    print("\nFilmes disponíveis:")
    print("1 - Panico 7")
    print("2 - Michael")
    print("3 - Homem-Aranha")
    print("4 - Gente Grande")
    print("5 - Deadpool 2")
    print("6 - Jurassic Park 3")
    print("7 - De Volta Para o Futuro")

    opcao = input("Escolha o número do filme: ")

    if opcao == "1":
        filme = "Panico 7"
        valor = 30
    elif opcao == "2":
        filme = "Michael"
        valor = 25
    elif opcao == "3":
        filme = "Homem-Aranha"
        valor = 20
    elif opcao == "4":
        filme = "Gente Grande"
        valor = 25
    elif opcao == "5":
        filme = "Deadpool 2"
        valor = 35
    elif opcao == "6":
        filme = "Jurassic Park 3"
        valor = 25
    elif opcao == "7":
        filme = "De Volta Para o Futuro"
    else:
        print("Opção inválida!")
        filme = "Nenhum"
        valor = 0

    return filme, valor


# Função para calcular valor total
def calcular_valor(valor_ingresso):
    quantidade = int(input("\nQuantidade de ingressos: "))
    total = valor_ingresso * quantidade
    return quantidade, total


# Função de pagamento
def pagamento():
    print("\nFormas de pagamento:")
    print("1 - Pix")
    print("2 - Cartão")
    print("3 - Dinheiro")

    forma = input("Escolha a forma de pagamento: ")

    if forma == "1":
        return "Pix"
    elif forma == "2":
        return "Cartão"
    elif forma == "3":
        return "Dinheiro"
    else:
        return "Forma inválida"


# Função para finalizar compra
def finalizar_compra(nome, filme, quantidade, total, forma_pagamento):
    print("\n===== COMPRA FINALIZADA =====")
    print("Cliente:", nome)
    print("Filme:", filme)
    print("Quantidade de ingressos:", quantidade)
    print("Valor total: R$", total)
    print("Pagamento:", forma_pagamento)
    print("✅ Compra realizada com sucesso!")
    print("=============================")


# Programa principal
nome_cliente = menu()

filme_escolhido, valor_filme = escolher_filme()

quantidade_ingressos, valor_total = calcular_valor(valor_filme)

forma_pagamento = pagamento()

finalizar_compra(
    nome_cliente,
    filme_escolhido,
    quantidade_ingressos,
    valor_total,
    forma_pagamento
)