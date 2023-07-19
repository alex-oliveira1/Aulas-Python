# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'
def substituir_caracteres(texto):
    texto = texto.replace('a', '4')
    texto = texto.replace('e', '3')
    texto = texto.replace('I', '1')
    texto = texto.replace('t', '7')
    return texto

entrada = input("Digite uma string: ")
nova_string = substituir_caracteres(entrada)

print("Nova string após substituição: ", nova_string)
