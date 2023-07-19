# 4.Faça um programa que recebe uma string e retorna ela ao contrário. Exemplo: Recebe "teste" e retorna "etset".
def inverter_string(texto):
    return texto[::-1]

entrada = input("Digite uma string: ")
string_invertida = inverter_string(entrada)

print("String invertida:", string_invertida)
