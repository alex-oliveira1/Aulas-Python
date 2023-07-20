# Importando o módulo 're' para utilizar expressões regulares
import re

# Dicionário para armazenar os fornecedores (chave: código do fornecedor, valor: informações do fornecedor)
fornecedores = {}

# Função para validar o formato do e-mail
def validar_email(email):
    padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(padrao_email, email)

# Função para adicionar fornecedores ao cadastro
def adicionar_fornecedor():
    codigo = input("Digite o código do fornecedor: ")
    nome = input("Digite o nome do fornecedor: ")
    telefone = input("Digite o telefone do fornecedor (11 dígitos): ")
    while not telefone.isdigit() or len(telefone) != 11:
        print("Telefone inválido. Deve conter exatamente 11 dígitos.")
        telefone = input("Digite o telefone do fornecedor (11 dígitos): ")
    
    email = input("Digite o email do fornecedor: ")
    while not validar_email(email):
        print("E-mail inválido. Digite um e-mail válido.")
        email = input("Digite o email do fornecedor: ")
    
    fornecedores[codigo] = {
        "Nome": nome,
        "Telefone": telefone,
        "Email": email
    }
    print("Fornecedor cadastrado com sucesso!")

# Função para exibir as informações de um fornecedor específico
def exibir_fornecedor():
    codigo = input("Digite o código do fornecedor que deseja exibir: ")
    fornecedor = fornecedores.get(codigo)
    if fornecedor:
        print("Código:", codigo)
        for chave, valor in fornecedor.items():
            print(chave + ":", valor)
    else:
        print("Fornecedor não encontrado.")

# Função para remover fornecedor do cadastro
def remover_fornecedor():
    if not fornecedores:
        print("Não há fornecedores cadastrados para remover.")
        return
    
    codigo = input("Digite o código do fornecedor que deseja remover: ")
    if codigo in fornecedores:
        del fornecedores[codigo]
        print("Fornecedor removido com sucesso!")
    else:
        print("Fornecedor não encontrado.")

# Função para exibir todos os fornecedores cadastrados
def exibir_todos_fornecedores():
    if not fornecedores:
        print("Não há fornecedores cadastrados.")
        return
    
    for codigo, fornecedor in fornecedores.items():
        print("Código:", codigo)
        for chave, valor in fornecedor.items():
            print(chave + ":", valor)
        print("-" * 20)

# Loop principal do sistema
while True:
    print("\n===== Sistema de Cadastro de Fornecedores =====")
    print("1 - Adicionar fornecedor")
    print("2 - Exibir informações de um fornecedor")
    print("3 - Remover fornecedor")
    print("4 - Exibir todos os fornecedores cadastrados")
    print("0 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == "1":
        adicionar_fornecedor()
    elif opcao == "2":
        exibir_fornecedor()
    elif opcao == "3":
        remover_fornecedor()
    elif opcao == "4":
        exibir_todos_fornecedores()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
