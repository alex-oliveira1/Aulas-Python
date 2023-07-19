# 6. Escreva um programa que receba um texto e uma palavra, então verifique se a palavra está no texto..
def verificar_palavra_no_texto(texto, palavra):
    texto_em_minusculo = texto.lower()
    palavra_em_minusculo = palavra.lower()

    return palavra_em_minusculo in texto_em_minusculo

texto_usuario = input("Digite um texto: ")
palavra_usuario = input("Digite uma palavra para verificar no texto: ")

if verificar_palavra_no_texto(texto_usuario, palavra_usuario):
    print("A palavra '{}' está presente no texto.".format(palavra_usuario))
else:
    print("A palavra '{}' NÃO está presente no texto.".format(palavra_usuario))
