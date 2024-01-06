def atendimento():
    lista = {}
    while True:
        desejo = ["adicionar item", "remover item", "ver lista", "sair"]
        pergunta = input("Qual ação deseja? ")
        while pergunta not in desejo:
            pergunta = input("Qual ação deseja? ")
        match pergunta.lower():
            case "adicionar item":
                adicionar_remover_item(lista, "adicionar")
            case "ver lista":
                ler_dicionario(lista)
            case "remover item":
                adicionar_remover_item(lista, "remover")
            case "sair":
                print("Volte sempre! ")
                break


def ler_dicionario(dicionario):
    if len(dicionario) == 0:
        print("Não tem itens na lista!")
    else:
        print("Sua lista contém: ")
        for indice, (key, valor) in enumerate(lista.items()):
            print(f"{indice} - {key} - {valor}")


def adicionar_remover_item(dicionario, opcao):
    match opcao.lower():
        case "adicionar":
            item = input("Qual item deseja adicionar? ").lower()
            quantidade = int(input("Quantos? "))
            if item in dicionario:
                dicionario[item] += quantidade
            else:
                dicionario[item] = quantidade
        case "remover":
            if len(dicionario) != 0:
                item = input("Qual item deseja remover? ").lower()
                while item not in dicionario:
                    item = input("Diga outro item, este item não esta na lista")
                    quantidade = int(input("Quantos? "))
                    if item in dicionario:
                        dicionario[item] -= quantidade
                        if dicionario[item] <= 0:
                            dicionario.pop(item)
            else:
                print("Não tem itens na lista")


""""------------------------------------------------------------------------"""


def previsao_venda_lojinha():
    previsoes_venda = {}
    while True:
        produto = input("Qual o nome do produto? ")
        if produto.strip() != "sair":
            try:
                venda = int(input("Quantos venderam? "))
                crescimento = int(input("Quantos por cento aumentou as vendas? "))
            except (TypeError, ValueError):
                print("Erro de dados, por favor digite um número.")
                break
            previsoes_venda[produto] = [venda, crescimento]
        else:
            for indice, (chave, (valor1, valor2)) in enumerate(previsoes_venda.items()):
                print(
                    f"{indice} - a previsão de vendas de {chave} será no próximo mês de: R${valor1 + (valor2/100)*valor1}))"
                )
            break


"""--------------------------------------------------------------------------"""


def solicitar_nome_vendedor(dicionario):
    """Retorna o nome do vendedor que está sendo buscado."""
    nomes = ""
    for chave, valor in dicionario.items():
        print(chave)


def solicitar_vendas(dicionario):
    nome = input("Diga o nome do vendedor ")
    if nome not in dicionario:
        print("Não temos este vendedor")
    else:
        print(f"{nome} teve uma venda de R${(dicionario[nome]):.2f}")


def atualizar_dados(dicionario):
    vendedor = input("Diga o nome do vendedor: ")
    if vendedor.strip() != "sair":
        valor_vendas = int(input("Qual o valor arrecadado? "))
        print("")
        if vendedor in dicionario:
            dicionario[vendedor] += valor_vendas
        else:
            dicionario[vendedor] = valor_vendas


def print_dados(dicionario):
    if len(dicionario) != 0:
        acumulador = 0
        pessoas = 0
        for chave, valor in dicionario.items():
            print(f"O vendedor {chave} arrecadou R${(valor):.2f}")
            acumulador += valor
            pessoas += 1
        print("")
        print(f"A media de vendas é de R${(acumulador/pessoas):.2f}")
    else:
        print("Nenhum dado foi cadastrado ainda.")


def atendimento_sistema():
    vendas_dos_vendedores = {}
    while True:
        valores = [
            "conhecer vendedores",
            "vendas",
            "atualizar dados",
            "saber valores",
            "sair",
        ]
        opcao = input(
            "Deseja: conhecer vendedores, vendas, atualizar dados, saber valores, sair "
        )
        while opcao.lower() not in valores:
            opcao = input(
                "Deseja: conhecer vendedores, vendas, atualizar dados, saber valores, sair "
            )
        match opcao.lower():
            case "conhecer vendedores":
                solicitar_nome_vendedor(vendas_dos_vendedores)
            case "vendas":
                solicitar_vendas(vendas_dos_vendedores)
            case "atualizar dados":
                atualizar_dados(vendas_dos_vendedores)
            case "saber valores":
                print_dados(vendas_dos_vendedores)
            case "sair":
                break


atendimento_sistema()
