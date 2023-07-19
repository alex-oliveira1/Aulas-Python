# 10.Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
# Se N for par, ele também deve ser incluído no output (vide exemplo para N = 2)
def imprimir_pares_decrescente(n):
    if n % 2 != 0:
        n -= 1

    while n >= -n:
        if n % 2 == 0:
            print(n, end=' ')
        n -= 2

numero_usuario = int(input("Digite um número inteiro (N): "))
print("Números pares entre {} e -{} (de forma decrescente):".format(numero_usuario, numero_usuario))
imprimir_pares_decrescente(numero_usuario)
