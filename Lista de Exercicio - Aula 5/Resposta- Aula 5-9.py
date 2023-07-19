# 9.Faça um script que informe o fatorial de um número.
# Utilize obrigatoriamente o comando for
def calcular_fatorial(numero):
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

numero_digitado = int(input("Digite um número para calcular o fatorial: "))

if numero_digitado < 0:
    print("O fatorial não está definido para números negativos.")
else:
    resultado = calcular_fatorial(numero_digitado)
    print("O fatorial de {} é: {}".format(numero_digitado, resultado))
