# 12. Faça um programa que recebe um número inteiro do usuário e imprime na tela a quantidade 
# de divisores desse número e quais são eles.
def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

numero_digitado = int(input("Digite um número inteiro: "))
divisores_encontrados = encontrar_divisores(numero_digitado)

print("\nQuantidade de divisores de {}: {}".format(numero_digitado, len(divisores_encontrados)))
print("Divisores de {}: {}".format(numero_digitado, divisores_encontrados))
