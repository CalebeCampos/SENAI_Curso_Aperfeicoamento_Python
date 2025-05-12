import os

try:
    
    dicionario = {}

    print("Infome o nome do usuario: ")
    nome = input("Nome: ")
    dicionario['nome'] = nome
    os.system('cls')

    print("Infome a data de nascimento do usuario: ")
    data_nascimento = input("Data de nascimento: ")
    dicionario['data_nascimento'] = data_nascimento
    os.system('cls')

    print("Infome o cpf do usuario: ")
    cpf = input("CPF: ")
    dicionario['cpf'] = cpf
    os.system('cls')

    print("Infome o email do usuario: ")
    email = input("Email: ")
    dicionario['email'] = email
    os.system('cls')

    print("Infome o genero do usuario: ")
    genero = input("Genero: ")
    dicionario['genero'] = genero
    os.system('cls')

    print("Infome o telefone do usuario: ")
    telefone = input("Telefone: ")
    dicionario['telefone'] = telefone
    os.system('cls')

    print("Infome o altura do usuario: ")
    altura = float(input("Altura: ").replace(',', '.'))
    dicionario['altura'] = altura
    os.system('cls')

    print("Infome o peso do usuario: ")
    peso = float(input("Peso: ").replace(',', '.'))
    dicionario['peso'] = peso
    os.system('cls')

    print("Infome o tipo sanguineo do usuario: ")
    tipo_sanguineo = input("Tipo sanguineo: ")
    dicionario['tipo_sanguineo'] = tipo_sanguineo
    os.system('cls')

    # Exibindo os dados do usuario
    print("\n")
    print(f"{'='*20}DADOS DO USUARIO{'='*20}\n")
    for chave in dicionario:
        print(f"{chave.title()}: {dicionario.get(chave)}")

    # Calculando o IMC
    imc = peso / (altura ** 2)

    print("\n")
    print(f"{dicionario['nome']} seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Você está abaixo do peso!")
    elif imc < 24.9:
        print("Você está com no peso normal!")
    else:
        print("Você está acima do peso!")

except Exception as e:
    print(f"Nao foi possivel inserir o dado informado. Erro: {e}")