# 6. Com base no dicionário obtido na questão anterior, faça:
# a) Uma função que retorne o número de homens e mulheres cadastrados;
def contar_homens_mulheres(dados_funcionarios):
    homens = 0
    mulheres = 0
    
    for funcionario in dados_funcionarios.values():
        if funcionario["Sexo"] == "M":
            homens += 1
        elif funcionario["Sexo"] == "F":
            mulheres += 1
            
    return homens, mulheres

# Exemplo de uso da função
dados_funcionarios = obter_dados_funcionarios()
num_homens, num_mulheres = contar_homens_mulheres(dados_funcionarios)
print("Número de homens:", num_homens)
print("Número de mulheres:", num_mulheres)

# b) Uma função que retorne um dicionário dos funcionários cujo tempo de serviço seja maior que 5 anos.
def funcionarios_tempo_servico_maior_que_5(dados_funcionarios):
    funcionarios_maior_que_5_anos = {}

    for matricula, funcionario in dados_funcionarios.items():
        if funcionario["TempoServiço"] > 5:
            funcionarios_maior_que_5_anos[matricula] = funcionario

    return funcionarios_maior_que_5_anos

# Exemplo de uso da função
dados_funcionarios = obter_dados_funcionarios()
funcionarios_maior_5_anos = funcionarios_tempo_servico_maior_que_5(dados_funcionarios)
print("Funcionários com tempo de serviço maior que 5 anos:")
print(funcionarios_maior_5_anos)

# c) Uma função que receba como argumento o sexo e retorne a média salarial dos funcionários daquele sexo.
def media_salarial_por_sexo(dados_funcionarios, sexo):
    total_salarios = 0
    total_funcionarios = 0

    for funcionario in dados_funcionarios.values():
        if funcionario["Sexo"] == sexo:
            total_salarios += funcionario["Salario"]
            total_funcionarios += 1

    if total_funcionarios == 0:
        return 0  # Evitar divisão por zero

    media_salarial = total_salarios / total_funcionarios
    return media_salarial

# Exemplo de uso da função
dados_funcionarios = obter_dados_funcionarios()
sexo_desejado = "M"  # Pode ser "F" para as mulheres
media_salarios_sexo = media_salarial_por_sexo(dados_funcionarios, sexo_desejado)
print(f"Média salarial dos funcionários do sexo {sexo_desejado}: {media_salarios_sexo:.2f}")
