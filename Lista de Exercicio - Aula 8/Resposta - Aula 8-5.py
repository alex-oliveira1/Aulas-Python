# 5.  Crie uma função e dê o nome pertinente para a mesma, essa função deve retornar um dicionário
# com os dados abaixo:
# Matricula - Nome      - Sexo - Departamento - TempoServiço - Salario
#     1     - Ana       -  F   -     TI       -      7       - 3200
#     2     - Beatriz   -  F   -     TI       -      4       - 3720
#     3     - Carla     -  F   -     TI       -      1       - 2100
#     4     - Daniela   -  F   -     RH       -      2       - 3920
#     5     - Emílio    -  M   -     RH       -      7       - 4235
#     6     - Fernando  -  M   -     RP       -      7       - 1200
#     7     - Gabriela  -  F   -     RP       -      8       - 7234.89
#     8     - Hernandes -  M   -     TI       -      6       - 4234.12
def obter_dados_funcionarios():
    dados = {
        1: {"Nome": "Ana", "Sexo": "F", "Departamento": "TI", "TempoServiço": 7, "Salario": 3200},
        2: {"Nome": "Beatriz", "Sexo": "F", "Departamento": "TI", "TempoServiço": 4, "Salario": 3720},
        3: {"Nome": "Carla", "Sexo": "F", "Departamento": "TI", "TempoServiço": 1, "Salario": 2100},
        4: {"Nome": "Daniela", "Sexo": "F", "Departamento": "RH", "TempoServiço": 2, "Salario": 3920},
        5: {"Nome": "Emílio", "Sexo": "M", "Departamento": "RH", "TempoServiço": 7, "Salario": 4235},
        6: {"Nome": "Fernando", "Sexo": "M", "Departamento": "RP", "TempoServiço": 7, "Salario": 1200},
        7: {"Nome": "Gabriela", "Sexo": "F", "Departamento": "RP", "TempoServiço": 8, "Salario": 7234.89},
        8: {"Nome": "Hernandes", "Sexo": "M", "Departamento": "TI", "TempoServiço": 6, "Salario": 4234.12}
    }
    return dados

# Exemplo de uso da função
dados_funcionarios = obter_dados_funcionarios()
print(dados_funcionarios)