import os

try:
    
    tupla = ('nome', 'data_nascimento', 'cpf', 'email', 'genero', 'telefone', 'altura', 'peso', 'tipo_sanguineo')
    dicionario = {}

    print("Infome o nome do usuario: ")
    dicionario[tupla[0]] = input("Nome: ")
    os.system('cls')

    print("Infome a data de nascimento do usuario: ")
    dicionario[tupla[1]] = input("Data de nascimento: ")
    os.system('cls')

    print("Infome o cpf do usuario: ")
    dicionario[tupla[2]] = input("CPF: ")
    os.system('cls')

    print("Infome o email do usuario: ")
    dicionario[tupla[3]] = input("Email: ")
    os.system('cls')

    print("Infome o genero do usuario: ")
    dicionario[tupla[4]] = input("Genero: ")
    os.system('cls')

    print("Infome o telefone do usuario: ")
    dicionario[tupla[5]] = input("Telefone: ")
    os.system('cls')

    print("Infome o altura do usuario: ")
    altura = float(input("Altura: ").replace(',', '.'))
    dicionario[tupla[6]] = altura
    os.system('cls')

    print("Infome o peso do usuario: ")
    peso = float(input("Peso: ").replace(',', '.'))
    dicionario[tupla[7]] = peso
    os.system('cls')

    print("Infome o tipo sanguineo do usuario: ")
    dicionario[tupla[8]] = input("Tipo sanguineo: ")
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