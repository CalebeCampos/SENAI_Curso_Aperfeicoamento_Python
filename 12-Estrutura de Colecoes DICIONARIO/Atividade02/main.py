"""
Crie um CRUD para:
- Cadastrar
- Listar
- Atualizar
- Deletar

O programa deverá cadastrar pessoas com os seguintes dados:
- Nome
- Email
- CPF
- Telefone
- Data de nascimento
- Genero

Observacoes:
- o usuario podera cadastrar quantas pessoas quiser
- o programa deverá fornecer um meno com as opcoes: cadastrar, listar, alterar, deletar e sair

"""


import os

lista = []
chaves = ["nome", "email", "cpf", "telefone", "data_nascimento", "genero"]

try:
    while True:
        # dados_pessoa = dict.fromkeys(chaves) # cria um dicionario com as chaves definidas na lista chaves
        dados_pessoa = {} # cria um dicionario vazio
        opcao_crud = input("Escolha um opção: 1-Cadastrar, 2-Listar, 3-Alterar, 4-Deletar, 5-Sair: ")
        os.system('cls')
        
        match opcao_crud:

            case "1":
                
                for i in range(len(chaves)):
                    dados_pessoa[chaves[i]] = input(f"Infome o(a) {chaves[i]} da pessoa:  ").strip().title()
                    os.system('cls')

                lista.append(dados_pessoa) # adiciona o dicionario pessoa na lista pessoas

                os.system('cls')
                print(f"Registro cadastrado com sucesso!\n")

                continue

            case "2":
                
                for elemento_lista in lista:
                    print(f"{'-'*20}\n")
                    for chave_dicionario in elemento_lista:
                        print(f"{chave_dicionario.title()}: {elemento_lista.get(chave_dicionario)}")
                print("\n")
                continue

            case "3":
                
                nome_pessoa_encontrar = input("Informe o NOME da pessoa que deseja alterar algum dado ou SAIR para finalizar: ").strip().title()

                match nome_pessoa_encontrar:

                    case 'SAIR':
                        os.system('cls')
                        print("Programa finalizado!")
                        break

                    case _:
                        
                        os.system('cls')
                        
                        for pessoa in lista:
                            
                            if pessoa.get("nome") == nome_pessoa_encontrar:
                                print(f"Registro encontrado!")
                                print("\n")
                                # imprimindo os dados da pessoa pesquisada pelo nome
                                for chave in pessoa:
                                    print(f"{chave.title()}: {pessoa.get(chave)}")
                                print("\n")

                                while True:
                                    
                                    atributo_pessoa_alterar = input("Informe o atributo que deseja atualizar: ").strip().lower()
                                    
                                    if atributo_pessoa_alterar in chaves:
                                        valor_informado_destino = input(f"Informe o novo valor para o(a) {atributo_pessoa_alterar}: ").strip().title()
                                        valor_informado_origem = pessoa.get(atributo_pessoa_alterar)
                                        #ATRIBUINDO O NOVO VALOR AO ATRIBUTO DO ELEMENTO ENCONTRADO
                                        pessoa[atributo_pessoa_alterar] = valor_informado_destino
                                        os.system('cls')
                                        print(f"O(A) {atributo_pessoa_alterar} da pessoa {nome_pessoa_encontrar} foi alterado de {valor_informado_origem} para {valor_informado_destino} com sucesso!")
                                        print("\n")
                                        break
                                    else:
                                        os.system('cls')
                                        print(f"O atributo {atributo_pessoa_alterar} nao existe!")
                                        print(f"Os atributos existentes sao: {chaves}")
                                        continue
                                    
                                continue
                                
                            elif pessoa.get("nome") != nome_pessoa_encontrar:
                                os.system('cls')
                                print(f"Nao foi possivel encontrar o registro da pessoa {nome_pessoa_encontrar}!")
                                break
                                

            case "4":
                
                nome_pessoa_encontrar = input("Informe o NOME da pessoa que deseja remover ou SAIR para finalizar: ").strip().title()

                match nome_pessoa_encontrar:

                    case 'SAIR':
                        os.system('cls')
                        print("Programa finalizado!")
                        break

                    case _:
                        
                        os.system('cls')
                        for pessoa in lista:
                            
                            if pessoa["nome"] == nome_pessoa_encontrar:
                                lista.remove(pessoa)
                                print(f"Registro da pessoa {nome_pessoa_encontrar} foi removido com sucesso!")
                                continue
                                
                            # else:
                            #     os.system('cls')
                            #     print(f"Nao foi possivel encontrar o registro da pessoa {nome_pessoa_encontrar}!")
                            #     break
                continue                             
                
            case "5":
                print("Saindo do programa...")
                break

            case _:
                print("Opcao invalida!")
                continue

except Exception as e:
    print(f"Nao foi possivel cadastrar, alterar, listar, deletar pessoa. Erro: {e}")
