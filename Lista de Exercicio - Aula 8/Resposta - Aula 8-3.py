# 3. Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor x inteiro como parâmetro e imprima uma linha com 1 até x. 
# Se x = 1 na função, imprime:
# 1
# Se x = 2 na função, imprime:
# 1   2
# E assim por diante.
def imprimir_linha(x):
    for i in range(1, x + 1):
        print(i, end="   ")
    print()  # Pular para a próxima linha após imprimir a sequência

def imprimir_padrao(n):
    for i in range(1, n + 1):
        imprimir_linha(i)

# Programa principal
try:
    n = int(input("Digite um número inteiro para gerar o padrão: "))
    imprimir_padrao(n)
except ValueError:
    print("Entrada inválida. Certifique-se de digitar um número inteiro.")
