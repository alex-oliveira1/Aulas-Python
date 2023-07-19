# 1. Construa um programa no qual o usuário informe o nome, a estatura e o peso de vários alunos
# de uma turma. Após o cadastro, o programa deve imprimir o nome e o IMC de cada aluno ordenados
# pelo nome do aluno. Sabe-se que IMC = peso/altura**2
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

turma = []
quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))

for i in range(quantidade_alunos):
    nome = input("Digite o nome do aluno: ")
    estatura = float(input("Digite a estatura do aluno (em metros): "))
    peso = float(input("Digite o peso do aluno (em quilogramas): "))

    imc = calcular_imc(peso, estatura)
    turma.append((nome, imc))

# Ordenar a turma pelo nome do aluno
turma.sort(key=lambda aluno: aluno[0])

# Imprimir o nome e IMC de cada aluno
print("\nNomes e IMC dos alunos (ordenados pelo nome):")
for aluno in turma:
    print("Nome:", aluno[0], " - IMC:", aluno[1])
