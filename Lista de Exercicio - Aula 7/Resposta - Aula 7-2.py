# 2. Faça um script que receba os valores do nome, idade e e-mail de uma pessoa
# e guarde-os em um dicionário com as chaves ‘nome’, ‘idade’ e ‘email’, respectivamente. 
# Exiba as informações desse dicionário
pessoa = {}

pessoa['nome'] = input("Digite o nome da pessoa: ")
pessoa['idade'] = int(input("Digite a idade da pessoa: "))
pessoa['email'] = input("Digite o e-mail da pessoa: ")

print("\nInformações da pessoa:")
print("Nome:", pessoa['nome'])
print("Idade:", pessoa['idade'])
print("E-mail:", pessoa['email'])
