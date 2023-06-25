# 3. Partindo da solução da questão anterior. Crie um programa que calcule o quadrado de um número quando ele for par e que calcule o cubo do número caso ele seja ímpar.
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    resultado = numero ** 2
    print("O quadrado do número é:", resultado)
else:
    resultado = numero ** 3
    print("O cubo do número é:", resultado)
