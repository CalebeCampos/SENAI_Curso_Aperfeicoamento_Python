import os

pessoas = []

try:
    while True:
        cadastrar = input("Deseja cadastrar nova pessoa? (s/n): ")
        
        match cadastrar:

            case 's':
                pessoa = {}
                pessoa["nome"] = input("Informe o nome da pessoa: ")
                pessoa["email"] = input("Informe o email da pessoa: ")
                pessoa["cpf"] = input("Informe o cpf da pessoa: ")

                pessoas.append(pessoa) # adiciona o dicionario pessoa na lista pessoas

                os.system('cls')
                print(f"{pessoa.get('nome')} cadastrado com sucesso!")

                for pessoa in pessoas:
                    print(f"\n{'-'*20}\n")
                    for chave in pessoa:
                        print(f"{chave.title()}: {pessoa.get(chave)}")

                continue

            case 'n':
                break
            case _:
                print("Opcao invalida!")
                continue

except Exception as e:
    print(f"Nao foi possivel cadastrar pessoa. Erro: {e}")