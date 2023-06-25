# 5. Escreva um programa que pergunte o valor inicial de uma dívida, o juro mensal. Pergunte também o valor mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
valor_inicial = float(input("Digite o valor inicial da dívida: "))
juro_mensal = float(input("Digite o juro mensal (em %): "))
valor_mensal = float(input("Digite o valor mensal a ser pago: "))

total_pago = 0
total_juros = 0
meses = 0

while valor_inicial > 0:
    juros = valor_inicial * (juro_mensal / 100)
    total_juros += juros
    valor_inicial += juros
    valor_inicial -= valor_mensal
    total_pago += valor_mensal
    meses += 1

print(f"Número de meses para pagar a dívida: {meses}")
print(f"Total pago: R$ {total_pago:.2f}")
print(f"Total de juros pago: R$ {total_juros:.2f}")
