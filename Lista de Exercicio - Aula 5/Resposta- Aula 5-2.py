# 2. Crie uma lista com os números pares de 0 a 20 e em seguida atenda os seguintes comandos:
# a) Inverta a ordem dos elementos da lista.
# b) Inverta a ordem dos elementos da lista.
# c) Remova os números múltimos de 5 da lista.
# Criar a lista com os números pares de 0 a 20
numeros_pares = [num for num in range(0, 21) if num % 2 == 0]

# a) Inverter a ordem dos elementos da lista
numeros_pares.reverse()

# b) Imprimir a lista após a inversão
print("Lista após a inversão:", numeros_pares)

# c) Remover os números múltiplos de 5 da lista
numeros_pares = [num for num in numeros_pares if num % 5 != 0]

# d) Imprimir a lista após a remoção
print("Lista após a remoção dos múltiplos de 5:", numeros_pares)
