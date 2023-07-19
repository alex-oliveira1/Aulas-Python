# 7. Faça um programa que leia nome e idade de 5 pessoas e coloque os nomes em uma lista e as idades em outra. 
# Apresente as duas listas preenchidas.
# Criar listas para armazenar os nomes e idades
nomes = []
idades = []

# Loop para ler o nome e idade de 5 pessoas
for i in range(5):
    nome = input("Digite o nome da pessoa {}: ".format(i+1))
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))

    # Adicionar o nome e a idade às respectivas listas
    nomes.append(nome)
    idades.append(idade)

# Apresentar as duas listas preenchidas
print("\nNomes das pessoas:", nomes)
print("Idades das pessoas:", idades)
