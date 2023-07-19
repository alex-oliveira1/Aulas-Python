# 1. Escreva uma função que retorne o maior número entre dois números.
def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Exemplo de uso da função
numero1 = 10
numero2 = 25
resultado = maior_numero(numero1, numero2)
print("O maior número é:", resultado)
