# 7. Suponha que determinado usuário possua 2 logins em uma rede corporativa.
# Login 1
# usuario: jardim
# senha: flores1206
# Login 2
# usuario: cordeiro
# senha la1506
# Escreva um programa que valide o acesso do usuário na rede. Caso o par usuário e senha estejam corretos, o programa deve imprimir a mensagem: "Seja bem vindo!". Caso contrário, "Usuário e senha não conferem".
login1_usuario = "jardim"
login1_senha = "flores1206"

login2_usuario = "cordeiro"
login2_senha = "la1506"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if (usuario == login1_usuario and senha == login1_senha) or (usuario == login2_usuario and senha == login2_senha):
    print("Seja bem-vindo!")
else:
    print("Usuário e senha não conferem.")
