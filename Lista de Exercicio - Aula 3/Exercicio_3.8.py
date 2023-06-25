# 8. Uma mobiliária paga aos seus corretores um salário base de 1500 Reais. Além disso, uma comissão de 200,00 Reias por cada imóvel vendido e 5% do valor de cada venda. Construa um programa que solicite o nome do corretor, a quantidade de imóveis vendidos e o valor total de suas vendas. Ao fim, o programa deve calcular e escrever o salário final do corretor de imóveis.
nome_corretor = input("Digite o nome do corretor: ")
quantidade_imoveis_vendidos = int(input("Digite a quantidade de imóveis vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))

salario_base = 1500
comissao_por_imovel = 200
porcentagem_comissao = 0.05

valor_comissao = comissao_por_imovel * quantidade_imoveis_vendidos
valor_comissao += valor_total_vendas * porcentagem_comissao

salario_final = salario_base + valor_comissao

print("Nome do corretor:", nome_corretor)
print("Salário final:", salario_final)
