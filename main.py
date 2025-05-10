import mercado
import banco
import dados

print("Bem vindo ao supermaket do Python\n")

while True:
    print(f"Dinheiro na carteira: {dados.carteira}€")
    print("\nEscolha se deseja ir ao mercado ou ao banco (Digite 1 ou 2)")
    print("1. Mercado")
    print("2. Banco")
    
    opcao = input("Opção: ")
    if opcao not in ["1", "2"]:
        print("Opção inválida")
    else:
        if opcao == "1":
            mercado.verTodosOsProdutos()
        elif opcao == "2":
            banco.entrarNoBanco()
