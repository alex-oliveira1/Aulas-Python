# 4. Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos 
# de mercado e seus respectivos preços e os mostre na tela.
mercado = {}

for i in range(3):
    produto = input("Digite o nome do {}º produto: ".format(i + 1))
    preco = float(input("Digite o preço do {}º produto: R$ ".format(i + 1)))

    mercado[produto] = preco

print("\nProdutos e seus respectivos preços:")
for produto, preco in mercado.items():
    print("{}: R$ {:.2f}".format(produto, preco))
