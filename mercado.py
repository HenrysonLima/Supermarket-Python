import dados

listaDeCompras = []  
precoFinal = 0  

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def verProduto(self):
        global listaDeCompras, precoFinal
        print(f"\nProduto: {self.nome}")
        print(f"Preço: {self.preco}\n")
        add = input("Deseja adicionar esse produto à lista de compras? (S/N): ").lower()
        if add == "s":
            listaDeCompras.append(self.nome)
            precoFinal += self.preco 
            print(f"\nLista de compras: {listaDeCompras}")
            print(f"Preço total: {precoFinal}")
        elif add != "n":
            print("Por favor insira uma opção válida.")
            self.verProduto()

produtos = [
    Produto("Arroz", 12),
    Produto("Bolo", 15),
    Produto("Minecraft", 18),
    Produto("Cereais", 7),
    Produto("Farinha", 4),
    Produto("Ervilhas em lata", 5),
    Produto("Leite", 2),
    Produto("Sumo de Maçã", 3),
    Produto("Abacate", 1),
    Produto("Açúcar em pó", 6)
]

def menu(var):
    if 1 <= var <= 10:
        produtos[var - 1].verProduto()
    else:
        print("Opção inválida")

def comprar():
    global precoFinal
    if len(listaDeCompras) == 0:
        print("\nLista vazia")
    elif precoFinal <= dados.carteira:
        dados.carteira -= precoFinal
        dados.ultimaAlteracaoDeCarteiraNoMercado = True
        dados.ultimaAlteracaoDeCarteiraNoBanco = False
        print("\nCompra efetuada")
        print(f"Valor restante na carteira: {dados.carteira}")
    else:
        print("\nVocê não tem dinheiro suficiente, pobre")
        print(f"Valor restante na carteira: {dados.carteira}")

def verTodosOsProdutos():
    global listaDeCompras, precoFinal
    listaDeCompras = []  
    precoFinal = 0

    print("Sua lista de compras está vazia")

    while True:
        try:
            print("\n--- Produtos ---")
            for i, p in enumerate(produtos, 1):
                print(f"Produto {i}: {p.nome} - {p.preco}€")
            opcao = input("Selecione o produto que deseja ver (1-10) | (Para ir ao pagamento digite (Pagar)): ").lower()
            if opcao == "pagar":
                comprar()
                break
            menu(int(opcao))
        except ValueError:
            print("\nOpção inválida. Por favor, selecione um número de 1 a 10.\n")
