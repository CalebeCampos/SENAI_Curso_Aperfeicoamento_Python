import os

try:

    lista_de_pessoas = []
    chaves_do_dicionario = ["nome", "email", "cpf", "telefone", "data_nascimento", "genero"]

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
                for i in range(len(chaves_do_dicionario)):
                    pessoa[chaves_do_dicionario[i]] = input(f"Infome o(a) {chaves_do_dicionario[i]} da pessoa:  ").strip().title()
                lista_de_pessoas.append(pessoa) # adiciona o dicionario pessoa na lista pessoas
                os.system('cls')
                print("Registro cadastrado com sucesso!")
                print("\n")
                continue

            # LISTAR
            case "2":
                os.system('cls')            
                for elemento_lista in lista_de_pessoas:
                    print(f"{'-'*20}\n")
                    print(f"Posicao {lista_de_pessoas.index(elemento_lista)}: ")
                    for chave_dicionario in elemento_lista:
                        print(f"{chave_dicionario.title()}: {elemento_lista.get(chave_dicionario)}")
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
                    # realiza a alteracao do atributo da pessoa
                    atributo_pessoa_alterar = input("Informe o atributo que deseja atualizar: ").strip().lower()
                    if lista_de_pessoas[posicao_pessoa_alterar][atributo_pessoa_alterar]:
                        valor_informado_destino = input(f"Informe o novo valor para o(a) {atributo_pessoa_alterar}: ").strip().title()
                        valor_informado_origem = lista_de_pessoas[posicao_pessoa_alterar][atributo_pessoa_alterar]
                        lista_de_pessoas[posicao_pessoa_alterar][atributo_pessoa_alterar] = valor_informado_destino
                        print(f"O(A) {atributo_pessoa_alterar} da pessoa {lista_de_pessoas[posicao_pessoa_alterar].get('nome')} foi alterado de {valor_informado_origem} para {valor_informado_destino} com sucesso!")
                        print("\n")
                    else:
                        print("Dado nao encontrado!")
                        print("\n")
                    continue   
                        
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