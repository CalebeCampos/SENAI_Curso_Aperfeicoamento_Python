import os

try:
    
    tupla = ('nome', 'data_nascimento', 'cpf', 'email', 'genero', 'telefone', 'altura', 'peso', 'tipo_sanguineo')
    dicionario = {}

    for i in range(len(tupla)):
        print(f"Infome o(a) {tupla[i]} do usuario: ")
        if i == 6 or i == 7:
            dicionario[tupla[i]] = float(input(f"{tupla[i].title()}: ").replace(',', '.'))
        else:
            dicionario[tupla[i]] = input(f"{tupla[i].title()}: ")
        os.system('cls')
 
    # Exibindo os dados do usuario
    print("\n")
    print(f"{'='*20}DADOS DO USUARIO{'='*20}\n")
    for chave in dicionario:
        print(f"{chave.title()}: {dicionario.get(chave)}")

    # Calculando o IMC
    imc = dicionario['peso'] / (dicionario['altura'] ** 2)

    print("\n")
    print(f"{dicionario['nome']} seu IMC é: {imc:.2f}")
    if imc < 18.5:
        print("Você está abaixo do peso!")
    elif imc < 24.9:
        print("Você está no peso ideal!")
    else:
        print("Você está acima do peso!")



except Exception as e:
    print(f"Nao foi possivel inserir o dado informado. Erro: {e}")