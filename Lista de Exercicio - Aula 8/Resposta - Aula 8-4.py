# 4. Faça uma função que verifique se um valor é perfeito ou não.
# Um valor é dito perfeito quando ele é igual a soma dos seus divisores excetuando ele próprio.
# (Ex: 6 é perfeito, 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar um valor booleano.
def verificar_numero_perfeito(numero):
    soma_divisores = 0
    
    # Itera de 1 até o número - 1 para encontrar os divisores
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    
    # Verifica se a soma dos divisores é igual ao próprio número
    return soma_divisores == numero

# Exemplo de uso da função
numero_teste = 6
resultado = verificar_numero_perfeito(numero_teste)

if resultado:
    print(f"{numero_teste} é um número perfeito.")
else:
    print(f"{numero_teste} não é um número perfeito.")
