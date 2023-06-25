# 2. Escreva um programa em que o usuário informará qual o último número a imprimir. E esse programa deverá mostrar apenas os números ímpares entre 1 e o número definido pelo usuário.
ultimo_numero = int(input("Digite o último número a imprimir: "))

for numero in range(1, ultimo_numero + 1):
    if numero % 2 != 0:
        print(numero)
