# 2. Construa um programa que receba do usuário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido(em segundos). Ao fim, calcule a velocidade média.
# Obs.: velocidade_media = variação_do_deslocamento/tempo_percorrido
variacao_deslocamento = float(input("Digite a variação do deslocamento (em metros): "))
variacao_tempo = float(input("Digite a variação do tempo percorrido (em segundos): "))

velocidade_media = variacao_deslocamento / variacao_tempo

print("A velocidade média é:", velocidade_media, "metros por segundo.")
