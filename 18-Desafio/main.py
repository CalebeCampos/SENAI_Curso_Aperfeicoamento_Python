import os
import random

lista_nomes = []

try:

    def sortear_nome(lista):
        return random.choice(lista)

    while True:

        print("=== Lista de Nomes ===")
        print("0 - SAIR")
        print("1 - Inserir nome")
        print("2 - Sortear um nome")
        print("3 - Exibir lista de nomes")
        print("======================")
        opcao = input("Escolha uma opção: ")
        os.system('cls') # Limpa a tela do terminal

        match opcao:
            case '0':
                os.system('cls') # Limpa a tela do terminal
                print("Programa encerrado.")
                break
            case '1':
                os.system('cls') # Limpa a tela do terminal
                while True:
                    os.system('cls') # Limpa a tela do terminal
                    print("0 - Voltar ao menu principal")
                    print("1 - Inserir nome")
                    opcao_inserir = input("Escolha uma opção: ")
                    os.system('cls') # Limpa a tela do terminal
                    match opcao_inserir:
                        case '0':
                            break
                        case '1':
                            nome = input("Informe um nome: ")
                            if nome:
                                lista_nomes.append(nome)
                                print(f"Nome '{nome}', adicionado com sucesso!")
                            else:
                                print("Nome não pode ser vazio.")
                            continue
                        case _:
                            print("Opção inválida. Tente novamente.")
                            continue
                continue
                    
            case '2':
                os.system('cls') # Limpa a tela do terminal
                if not lista_nomes:
                    print("Nenhum nome cadastrado para sortear.")
                else:
                    print(f"Nome sorteado: {sortear_nome(lista_nomes)}")
            
            case '3':
                os.system('cls')
                if not lista_nomes:
                    print("Nenhum nome cadastrado.")
                else:
                    print("Lista de nomes...")
                    for n in range(len(lista_nomes)):
                        print(f"{n+1}: {lista_nomes[n]}")
                continue

            case _:
                os.system('cls') # Limpa a tela do terminal
                print("Opção inválida. Tente novamente.")      
   
except Exception as e:
    print(f"Nao foi possivel executar o programa. Erro: {e}")


