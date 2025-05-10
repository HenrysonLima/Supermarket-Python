import dados

class ContaCorrente:
    def __init__(self, saldo, limite):
        self.saldo = saldo
        self.limite = limite

    def levantar(self):
        try:
            valor = int(input("Valor que deseja levantar: "))
            if valor <= self.saldo:
                self.saldo -= valor
                dados.carteira += valor
                dados.ultimaAlteracaoDeCarteiraNoBanco = True
                dados.ultimaAlteracaoDeCarteiraNoMercado = False
                print("Levantamento executado com sucesso\n")
            else:
                print("Saldo insuficiente\n")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    def fazerEmprestimo(self):
        try:
            valor = int(input("Valor do empréstimo: "))
            if valor <= self.limite:
                self.limite -= valor
                dados.carteira += valor
                dados.ultimaAlteracaoDeCarteiraNoBanco = True
                dados.ultimaAlteracaoDeCarteiraNoMercado = False
                print(f"Retirado {valor}€ do limite")
            else:
                print("Sem limite no cartão\n")
        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    def consultarSaldo(self):
        print(f"\nO saldo atual da sua conta é de: {self.saldo}€")

    def verificar_limite(self):
        print(f"O seu limite é de: {self.limite}€")

conta1 = ContaCorrente(30, 100)

def entrarNoBanco():
    print("\nBem vindo ao banco.")
    while True:
        conta1.consultarSaldo()
        conta1.verificar_limite()
        print("\nO que gostaria de fazer?")
        print("1. Fazer levantamento de dinheiro")
        print("2. Fazer um empréstimo")
        print("3. Sair do banco")
        try:
            opcao = int(input("Opção (digite 1, 2 ou 3): "))
            print("")
            if opcao == 1:
                conta1.levantar()
            elif opcao == 2:
                conta1.fazerEmprestimo()
            elif opcao == 3:
                break
            else:
                print("Opção inválida.")
            print(f"Tem {dados.carteira}€ na carteira.")
        except ValueError:
            print("Por favor, insira uma opção válida.")
