import os
import random

if __name__ == "__main__":

    try:

        contas_cadastradas = []

        while True:

            print(f"{"="*20} SISTEMA BANCARIA {"="*20}")
            print("\n")
            print("1 - Criar conta")
            print("2 - Consular contas")
            print("3 - Alterar cadastro do titular da conta")
            print("4 - Excluir conta")
            print("5 - Sacar")
            print("6 - Depositar")
            print("7 - Consultar saldo")
            print("0 - Sair")
            opcao = int(input("Opcao desejada: "))
            conta = {}

            match opcao:

                case 1: # CADASTRAR CONTA
                    os.system('cls')
                    nome = input("Informe o nome do titular da conta: ")
                    cpf = input("Informe o CPF do titular da conta: ")
                    conta["Titular_Nome"] = nome
                    conta["Titular_CPF"] = cpf
                    conta["Agencia"] = "1010"
                    conta["Numero"] = random.randint(1000000000, 9999999999)
                    conta["Saldo"] = 0
                    contas_cadastradas.append(conta)
                    print(f"Conta {conta.get("Numero")} cadastrada com sucesso!")
                    print("\n")
                    continue

                case 2: # CONSULTAR CONTAS CADASTRADAS
                    os.system('cls')
                    for conta in range(len(contas_cadastradas)):
                        print(f"Posicao {conta}:")
                        for chave in contas_cadastradas[conta]:
                            print(f"{chave}: {contas_cadastradas[conta].get(chave)}")
                        print("\n")
                    continue                    
                    
                case 3: # ALTERAR TITULAR DA CONTA
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
                        
                        while True:
                            
                            print("Informe o que deseja alterar...")
                            print("1 - Nome do titular")
                            print("2 - CPF do titular")
                            print("0 - Para voltar ao menu principal.")
                            print("\n")
                            opcao_titular_escolhida = int(input("Opção desejada: "))
                            
                            match opcao_titular_escolhida:
                                case 1: 
                                    # altera o nome do titular e cpf do titular da conta
                                    novo_titular_nome = input("Informe o nome do novo titular: ")
                                    contas_cadastradas[indice_conta_alterar]["Titular_Nome"] = novo_titular_nome
                                    print(f"Nome do titular alterado com sucesso!")
                                    print("\n")
                                    continue
                                
                                case 2:
                                    # altera o CPF do titular e cpf do titular da conta
                                    novo_titular_cpf = input("Informe o CPF do novo titular: ")
                                    contas_cadastradas[indice_conta_alterar]["Titular_CPF"] = novo_titular_cpf
                                    print(f"CPF do titular alterado com sucesso!")
                                    print("\n")
                                    continue
                                
                                case 0:
                                    break

                                case _:
                                    print("Opcao invalida!")
                                    print("\n")
                                    continue
                                
                    else:
                        print("Conta nao encontrada!")
                        print("\n")

                    continue

                case 4: # EXCLUIR CONTA
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

                case 5: # SACAR
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
                        
                        while True:
                            
                            print("Informe o que deseja fazer...")
                            print("1 - Informar valor para saque.")
                            print("0 - Voltar ao menu principal.")
                            print("\n")
                            opcao_saque_escolhido = int(input("Opcao desejada: "))
                            
                            match opcao_saque_escolhido:
                                
                                case 1:  
                                    # subtrai o valor informado pelo usuario do saldo da conta escolhida
                                    valor_saque = float(input("Valor a ser sacado: ").replace(",","."))
                                    if valor_saque > 0:
                                        if valor_saque <= contas_cadastradas[indice_conta_sacar].get("Saldo"):
                                            novo_saldo = (contas_cadastradas[indice_conta_sacar].get("Saldo") - valor_saque)
                                            contas_cadastradas[indice_conta_sacar]["Saldo"] = novo_saldo
                                            print("\n")
                                            print(f"Valor R$ {valor_saque} sacado com sucesso!")
                                            print(f"Seu novo saldo é R$ {novo_saldo}")
                                            print("Retire as cedulas da maquina...")
                                            print("\n")
                                        else:
                                            print("Valor maior que o saldo!")
                                            print(f"Saldo R$ {contas_cadastradas[indice_conta_sacar]["Saldo"]}")
                                            print("\n")
                                        
                                    else:
                                        print("Informe um valor maior que zero!")
                                    
                                    continue
                                
                                case 0:
                                    break
                                
                                case _:
                                    print("Opcao invalida!")
                                    print("\n")
                                    continue                           
                                
                            continue
                            
                    else:
                        print("Conta nao encontrada!")
                        print("\n")
                    continue

                case 6: # DEPOSITAR
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
                        valor_deposito = float(input("Informe o valor a ser depositado: ").replace(",","."))
                        novo_saldo = (contas_cadastradas[indice_conta_depositar].get("Saldo") + valor_deposito)
                        contas_cadastradas[indice_conta_depositar]["Saldo"] = novo_saldo
                        print(f"Valor R$ {valor_deposito} depositado com sucesso!")
                        print("\n")
                    else:
                        print("Conta nao encontrada!")
                        print("\n")
                    continue

                case 7: # CONSULTAR SALDO
                    os.system('cls')
                    
                    indice_conta_consultar_saldo = int(input("Informe a posicao da conta que deseja consultar o saldo: "))

                    if contas_cadastradas[indice_conta_consultar_saldo]:
                        os.system('cls')
                        print("Registro encontrado!")
                        print("\n")
                        # imprime o saldo da conta pesquisada pela posicao na lista
                        print(f"Titular_Nome: {contas_cadastradas[indice_conta_consultar_saldo].get("Titular_Nome")}")
                        print(f"Numero: {contas_cadastradas[indice_conta_consultar_saldo].get("Numero")}")
                        print(f"SALDO: {contas_cadastradas[indice_conta_consultar_saldo].get("Saldo")}")
                        print("\n")
                    else:
                        print("Conta nao encontrada!")
                        print("\n")
                    continue

                case 0: # SAIR
                    os.system('cls')
                    print("Programa finalizado!")
                    break

                case _:
                    os.system('cls')
                    print("Opção invalida!")
                    print("\n")
                    continue


    except Exception as e:
        print(f"Nao foi possivel cadastrar a conta bancaria. Erro: {e}")