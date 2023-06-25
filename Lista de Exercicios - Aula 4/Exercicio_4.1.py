# 1. Desenvolva um programa que leia dois números e informe o maior deles.
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    maior = numero1
else:
    maior = numero2

print("O maior número é:", maior)
