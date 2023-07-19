# 6. Crie um dicionário vazio semana = {} e o complete com uma chave para cada dia da semana, tendo
#  como seu valor uma lista com as aulas que você tem nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?).
semana = {
    'segunda': ['Matemática', 'História'],
    'terça': ['Português', 'Biologia'],
    'quarta': ['Física', 'Química'],
    'quinta': ['Geografia', 'Inglês'],
    'sexta': ['Artes', 'Educação Física'],
    'sábado': [],
    'domingo': []
}

# Para adicionar aulas de sábado e domingo, basta adicionar à lista vazia.
# Por exemplo:
# semana['sábado'] = ['Aula de dança']
# semana['domingo'] = ['Aula de música']

print("Aulas da semana:")
for dia, aulas in semana.items():
    print("{}: {}".format(dia.capitalize(), ', '.join(aulas) if aulas else 'Sem aulas'))
