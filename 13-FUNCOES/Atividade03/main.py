"""
Crie um programa onde o usuario faz um cadastro de uma conta em uma instituicao bancaria, e apos esse cadastro, o programa exibe o seguinte menu:
0 - Sair
1 - Criar conta bancaria
2 - Alterar cadastro do titular da conta
3 - Excluir conta
4 - Sacar
5 - Depositar
6 - Consultar saldo
    Dados do titular da conta:
    nome
    CPF
    agencia (1010)
    numero da conta (numero aleatorio)
    saldo (iniciar com zero)
obs: para gerar numero aleatorio da conta, usar a biblioteca random
"""
import os
import random

if __name__ == "__main__":

    try:

        conta = {}
        contas_cadastradas = []

        while True:

            print(f"{"="*20} CADASTRO DE CONTA BANCARIA {"="*20}")
            print("\n")
            print("1 - Criar conta bancaria")
            print("2 - Alterar cadastro do titular da conta")
            print("3 - Excluir conta")
            print("4 - Sacar")
            print("5 - Depositar")
            print("6 - Consultar saldo")
            print("0 - Sair")
            opcao = int(input("Escolha uma opção: "))

            match opcao:

                case 1: # CADASTRAR CONTA
                    os.system('cls')
                    nome = print("Informe o nome do titular da conta: ")
                    cpf = print("Informe o CPF do titular da conta: ")
                    conta["Titular_Nome"] = nome
                    conta["Titular_CPF"] = cpf
                    conta["Agencia"] = "1010"
                    conta["Numero"] = random.randint(1000000000, 9999999999)
                    conta["Saldo"] = 0
                    contas_cadastradas.append(conta)
                    continue

                case 2: # ALTERAR TITULAR DA CONTA
                    os.system('cls')
                    indice_conta_alterar = int(input("Informe a posicao da conta que deseja alterar: "))

                    if contas_cadastradas[indice_conta_alterar]:
                        os.system('cls')
                        print(f"Registro encontrado!")
                        print("\n")
                        # imprime os dados da conta pesquisada pela posicao na lista
                        for chave in contas_cadastradas[indice_conta_alterar]:
                            print(f"{chave.title()}: {contas_cadastradas[indice_conta_alterar].get(chave)}")
                        print("\n")
                        # altera o nome do titular e cpf do titular da conta
                        novo_titular_nome = print("Informe o nome do novo titular: ")
                        novo_titular_cpf = print("Informe o CPF do novo titular: ")
                        contas_cadastradas[indice_conta_alterar]["Titular_Nome"] = novo_titular_nome
                        contas_cadastradas[indice_conta_alterar]["Titular_CPF"] = novo_titular_cpf
                        print(f"Conta alterada com sucesso!")
                        print("\n")

                    else:
                        print("Conta nao encontrada!")
                        print("\n")

                    continue

                case 3: # EXCLUIR CONTA
                    os.system('cls')
                    indice_conta_deletar = int(input("Informe a posicao da conta que deseja deletar: "))

                    if contas_cadastradas[indice_conta_deletar]:
                        del(contas_cadastradas[indice_conta_deletar])
                        print(f"Conta deletada com sucesso!")
                        print("\n")
                    else:
                        print("Conta nao encontrada!")
                        print("\n")
                    continue

                case 4: # SACAR
                    os.system('cls')
                    indice_conta_sacar = int(input("Informe a posicao da conta que deseja sacar: "))

                    if contas_cadastradas[indice_conta_sacar]:
                        os.system('cls')
                        print(f"Registro encontrado!")
                        print("\n")
                        # imprime os dados da conta pesquisada pela posicao na lista
                        for chave in contas_cadastradas[indice_conta_sacar]:
                            print(f"{chave.title()}: {contas_cadastradas[indice_conta_sacar].get(chave)}")
                        print("\n")
                        # subtrai o valor informado pelo usuario do saldo da conta escolhida
                        valor_saque = float(print("Informe o valor a ser sacado: ").replace(",","."))
                        if valor_saque <= contas_cadastradas[indice_conta_sacar].get("Saldo"):
                            novo_saldo = (contas_cadastradas[indice_conta_sacar].get("Saldo") - valor_saque)
                            contas_cadastradas[indice_conta_sacar]["Saldo"] = novo_saldo
                            print(f"Valor R$ {valor_saque} sacado com sucesso! Retire as cedulas da maquina.")
                        else:
                            print(f"Saldo R$ {contas_cadastradas[indice_conta_sacar]["Saldo"]} menor que o valor R$ {valor_saque} informado para saque!")
                    else:
                        print("Conta nao encontrada!")
                        print("\n")
                    continue

                case 5: # DEPOSITAR
                    os.system('cls')
                    indice_conta_depositar = int(input("Informe a posicao da conta que deseja depositar: "))

                    if contas_cadastradas[indice_conta_depositar]:
                        os.system('cls')
                        print(f"Registro encontrado!")
                        print("\n")
                        # imprime os dados da conta pesquisada pela posicao na lista
                        for chave in contas_cadastradas[indice_conta_depositar]:
                            print(f"{chave.title()}: {contas_cadastradas[indice_conta_depositar].get(chave)}")
                        print("\n")
                        # soma o valor informado pelo usuario ao saldo da conta escolhida
                        valor_deposito = float(print("Informe o valor a ser depositado: ").replace(",","."))
                        novo_saldo = (contas_cadastradas[indice_conta_depositar].get("Saldo") + valor_deposito)
                        contas_cadastradas[indice_conta_depositar]["Saldo"] = novo_saldo
                        print(f"Valor R$ {valor_deposito} depositado com sucesso!")
                    else:
                        print("Conta nao encontrada!")
                        print("\n")
                    continue

                case 6: # CONSULTAR SALDO
                    os.system('cls')
                    continue

                case 0: # SAIR
                    os.system('cls')
                    print("Programa finalizado!")
                    break

                case _:
                    os.system('cls')
                    print("Opção invalida!")
                    continue


    except Exception as e:
        print(f"Nao foi possivel cadastrar a conta bancaria. Erro: {e}")