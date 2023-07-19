# 11. Faça um script que peça ao usuário para digitar um número n e some todos os números de 1 a n.
def somar_ate_n(numero):
    soma = 0
    for i in range(1, numero + 1):
        soma += i
    return soma

numero_digitado = int(input("Digite um número inteiro (n): "))
resultado = somar_ate_n(numero_digitado)
print("A soma de todos os números de 1 a {} é: {}".format(numero_digitado, resultado))
