# 6. Escreva um programa que pergunte a distância que determinado passageiro deseja percorrer em km. A partir disso calcule o preço da passagem. É cobrado 0,50 centavos por km para viagens de até 300 km. E 0,45 centavos para viagens mais longas.
distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 300:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O preço da passagem é R$ {:.2f}".format(preco))
