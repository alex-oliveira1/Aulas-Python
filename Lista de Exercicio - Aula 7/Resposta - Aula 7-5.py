# 5. Escreva um programa que conta a quantidade de vogais em um 
# texto e armazena tal quantidade em um dicionário, onde a 
# chave é a vogal considerada.
def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador_vogais = {}

    for letra in texto:
        if letra in vogais:
            contador_vogais[letra] = contador_vogais.get(letra, 0) + 1

    return contador_vogais

texto_usuario = input("Digite um texto: ")
resultado = contar_vogais(texto_usuario)

print("\nQuantidade de vogais no texto:")
for vogal, quantidade in resultado.items():
    print("{}: {}".format(vogal, quantidade))
