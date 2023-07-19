# 8.Faça um script que leia números do usuário, enquanto ele não digitar 0. 
# Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0, 
# o valor máximo e o valor mínimo.
numeros = []
numero = int(input("Digite um número (digite 0 para sair): "))

while numero != 0:
    numeros.append(numero)
    numero = int(input("Digite um número (digite 0 para sair): "))

if len(numeros) > 0:
    quantidade_numeros = len(numeros)
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)

    print("\nQuantidade de números digitados (desconsiderando o 0):", quantidade_numeros)
    print("Valor máximo:", valor_maximo)
    print("Valor mínimo:", valor_minimo)
else:
    print("\nNenhum número foi digitado (exceto o 0).")
