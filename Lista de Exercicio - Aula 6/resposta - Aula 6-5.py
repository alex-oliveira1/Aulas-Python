# 5. Escreva um programa que duas strings e gere uma terceira na qual os caracteres da segunda foram retirados da primeira.
def remover_caracteres(string_original, caracteres_remover):
    for caractere in caracteres_remover:
        string_original = string_original.replace(caractere, '')
    return string_original

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string (caracteres a serem removidos): ")

nova_string = remover_caracteres(string1, string2)

print("Nova string após remoção de caracteres:", nova_string)
