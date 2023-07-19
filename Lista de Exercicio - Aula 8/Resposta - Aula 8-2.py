# 2. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverso_numero(numero):
    # Convertendo o número para uma string para facilitar a manipulação
    numero_str = str(numero)
    
    # Invertendo a string usando slicing
    numero_reverso_str = numero_str[::-1]
    
    # Convertendo a string resultante de volta para um número inteiro
    numero_reverso = int(numero_reverso_str)
    
    return numero_reverso

# Exemplo de uso da função
numero_original = 127
resultado = reverso_numero(numero_original)
print("O reverso do número {} é: {}".format(numero_original, resultado))
