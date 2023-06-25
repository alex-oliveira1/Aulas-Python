# 6. Faça um programa que peça o nome e a idade do usuário e que ao final informe o ano de nascimento da pessoa.
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_atual = 2023
ano_nascimento = ano_atual - idade

print("Seu nome é", nome)
print("Você nasceu no ano", ano_nascimento)
