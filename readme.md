# Supermarket Python
Este projeto foi desenvolvido como parte da formação acadêmica durante o 10º ano do curso profissional de programação, visando desenvolver e frisar:
- Fundamentos em Python
- Programação orientada a objetos (POO)
- Modularização em Python
- Trabalho colaborativo em equipa

## Sobre o projeto
O Supermarket Python é um simulador onde o utilizador tem a possibilidade de explorar dois estabelecimentos, cada um com suas devidas funcionalidades:

Banco:
- Realizar levantamentos
- Solicitar empréstimos
- Visualizar saldo e limite da conta

Mercado:
- Ver os produtos disponíveis
- Checar o preço de um produto de interesse
- Adicionar um produto ao carrinho de compras
- Pagar pelos produtos do carrinho

O saldo bancário influencia as compras no mercado, promovendo uma interação realista entre os dois ambientes.

## Pré-requisitos
Antes de executar o projeto, verifique se possui:
- Python instalado
- Um editor de código (VSCode por exemplo)

## Instalação e execução
1. Clone o repositório git
<code>git clone https://github.com/HenrysonLima/Supermarket-Python</code>

2. Aceda à pasta do projeto 
<code>cd Supermarket-Python</code>

3. Execute
<code>python main.py</code>

## Estrutura do código
**main.py:** Ficheiro principal. Faz a ligação entre os módulos e apresenta o menu ao utilizador.

**banco.py:** Contém as classes e métodos relacionados à gestão bancária.

**mercado.py:** Responsável pelas funcionalidades do mercado e carrinho de compras.

**dados.py:** Gerencia variáveis compartilhadas entre os módulos para sincronização de dados.