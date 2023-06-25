# 3. Imagine o sistema de um caixa eletrônico. Construa um programa que receba um senha e que essa senha tenha que ser validada. Considere que a senha é **123456**. Existem as seguintes restrições:
# - Ao acertar a senha, a mensagem a ser exibida é: "Olá! Seja bem-vindo ao banco!"
# - Quando o usuário errar a senha pela primeira vez, mostrar a mensagem: "Senha incorreta! Você ainda tem 2 tentativas."
# - Se o usuário errar a senha pela segunda vez, mostrar: "Senha incorreta! Você ainda tem 1 tentativa."
# - Se o usuário errar a senha novamente, mostrar a mensagem "Sua senha foi bloquada! Por favor, dirija-se a agência".
senha_correta = "123456"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Olá! Seja bem-vindo ao banco!")
        break
    else:
        tentativas -= 1
        if tentativas == 0:
            print("Sua senha foi bloqueada! Por favor, dirija-se à agência.")
        else:
            print("Senha incorreta! Você ainda tem", tentativas, "tentativas.")
