 #8. Uma empresa concederá aumento de salário aos seus funcionários de acordo com o #cargo.
# Cargo - Aumento(%)
# Gerente Geral - 30
# Gerente de Relacionamento - 30
# Analista - 25
# Assistente de Atendimento - 20
# Crie um programa que solicite o salário e o cargo do funcionário. O programa deve calcular e imprimir o novo salário. Caso o cargo informado não esteja na tabela, o programa deve imprimir "Cargo inválido".
salario = float(input("Digite o salário do funcionário: "))
cargo = input("Digite o cargo do funcionário: ")

aumento = 0

if cargo == "Gerente Geral" or cargo == "Gerente de Relacionamento":
    aumento = 30
elif cargo == "Analista":
    aumento = 25
elif cargo == "Assistente de Atendimento":
    aumento = 20
else:
    print("Cargo inválido")
    exit()

novo_salario = salario + (salario * aumento / 100)

print("O novo salário do funcionário é:", novo_salario)
