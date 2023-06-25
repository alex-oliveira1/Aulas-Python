# 5. Escreva um program que leia dois números e que pergunte qual operação o usuário deseja realizar. Esse programa deve aceitar como respostas a soma(+), a subtração(-), a multiplicação (*) e a divisão (/). Ao final, o programa deve exibir o resultado da operação escolhida.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    resultado = numero1 / numero2
else:
    print("Operação inválida!")
    exit()

print("O resultado da operação é:", resultado)
