import os

try:

    lista_de_pessoas = []

    while True:

        pessoa = {}

        print(f"{'='*20} Sistema de cadastro de pessoas {'='*20}")
        opcao = input("Escolha uma opção (0 - Sair, 1 - Cadastrar, 2 - Listar, 3 - Alterar, 4 - Deletar): ").strip()

        match opcao:

            case "0":
                print("Programa finalizado!")
                break

            # CADASTRAR
            case "1":
                os.system('cls')
                pessoa["nome"] = input("Informe o nome da pessoa: ").strip().title()
                pessoa["email"] = input("Informe o email da pessoa: ").strip().lower()
                pessoa["cpf"] = input("Informe o cpf da pessoa: ").strip()
                pessoa["telefone"] = input("Informe o telefone da pessoa: ").strip()
                pessoa["data_nascimento"] = input("Informe a data de nascimento da pessoa: ").strip()
                pessoa["genero"] = input("Informe o genero da pessoa: ").strip().title()
                lista_de_pessoas.append(pessoa)
                print("Registro cadastrado com sucesso!")
                print("\n")
                continue

            # LISTAR
            case "2":
                os.system('cls')
                for pessoa in range(len(lista_de_pessoas)):
                    print(f"Posicao {pessoa}:")
                    for chave in lista_de_pessoas[pessoa]:
                        print(f"{chave.title()}: {lista_de_pessoas[pessoa].get(chave)}")
                    print("\n")
                continue

            # ALTERAR
            case "3":
                os.system('cls')
                posicao_pessoa_alterar = int(input("Informe a posicao da pessoa que deseja alterar: "))

                if lista_de_pessoas[posicao_pessoa_alterar]:
                    os.system('cls')
                    print(f"Registro encontrado!")
                    print("\n")
                    # imprime os dados da pessoa pesquisada pela posicao na lista
                    for chave in lista_de_pessoas[posicao_pessoa_alterar]:
                        print(f"{chave.title()}: {lista_de_pessoas[posicao_pessoa_alterar].get(chave)}")
                    print("\n")

                    chave_escolhida = input("Informe o dado que deseja alterar: ").strip().lower()
                    if lista_de_pessoas[posicao_pessoa_alterar][chave_escolhida]:
                        novo_dado = input(f"Informe o novo valor: ")
                        # altera o dado da chave escolhida
                        lista_de_pessoas[posicao_pessoa_alterar][chave_escolhida] = novo_dado
                        print(f"Registro alterado com sucesso!")
                        print("\n")
                    else:
                        print("Dado nao encontrado!")
                        print("\n")
                else:
                    print("Pessoa nao encontrada!")
                    print("\n")
                continue

            # DELETAR
            case "4":
                os.system('cls')
                posicao_pessoa_deletar = int(input("Informe a posicao da pessoa que deseja deletar: "))
                if lista_de_pessoas[posicao_pessoa_deletar]:
                    del(lista_de_pessoas[posicao_pessoa_deletar])
                    print(f"Registro deletado com sucesso!")
                    print("\n")
                else:
                    print("Pessoa nao encontrada!")
                    print("\n")
                continue
                        

            case _:
                os.system('cls')
                print("Opcao invalida!")
                continue
 
except Exception as e:
    print(f"Nao foi possivel exevutar a operacao. Erro: {e}")