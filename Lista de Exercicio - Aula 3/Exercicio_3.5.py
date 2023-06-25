# 5. Escreva um programa que calcule um aumento de salário. No programa o usuário deve ser capaz de inserir o valor atual do salário, a porcentagem de aumento que receberá e o programa deverá informar ao final o novo valor do salário e qual o valor do acréscimo do salário.
salario_atual = float(input("Digite o valor atual do salário: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

acrescimo = salario_atual * (porcentagem_aumento / 100)
novo_salario = salario_atual + acrescimo

print("Novo salário:", novo_salario)
print("Acréscimo salarial:", acrescimo)
