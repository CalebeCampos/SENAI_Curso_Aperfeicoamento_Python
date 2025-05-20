import os
import random
import modulo as m

if __name__ == "__main__":
    
    conta = {}

    try:
        
        while True:

            print(f"{'='*20} MENU {'='*20}")
            print("0 - Sair")
            print("1 - Criar conta bancaria")
            print("2 - Alterar cadastro do titular da conta")
            print("3 - Sacar")
            print("4 - Depositar")
            print("5 - Consultar dados da conta")

            opcao = input("Opcao desejada: ")
            os.system('cls')

            match opcao:

                case "0":
                    print("Programa encerrado!")
                    break
                
                case "1":
                    os.system('cls')
                    conta["agencia"] = 1010
                    conta["conta"] = random.randint(10000, 99999)
                    conta["saldo"] = 0
                    conta["nome"] = input("Informe o nome do titular: ")
                    conta["cpf"] = input("Informe o CPF do titular: ")
                    os.system('cls')
                    print(f"Conta: {conta.get('conta')} cadastrada com sucesso!\n")
                    continue
                
                case "2":
                    os.system('cls')
                    print(f"Nome: {conta.get('nome')}")
                    print(f"CPF: {conta.get('cpf')}")
                    campo_alterar = input("Informe o campo a ser alterado (nome/cpf): ").lower().strip()
                    match campo_alterar:
                        case "nome":
                            conta["nome"] = input("Informe o novo nome do titular: ")
                            os.system('cls')
                            print("Nome do titular alterado com sucesso!")
                        case "cpf":
                            conta["cpf"] = input("Informe o novo CPF do titular: ")
                            os.system('cls')
                            print("CPF do titular alterado com sucesso!")
                        case _:
                            os.system('cls')
                            print("Campo invalido!")
                    continue

                case "3":
                    os.system('cls')
                    valor_sacar = float(input("Informe o valor a ser sacado: R$ ").replace(",", "."))
                    saldo = conta.get("saldo")
                    if valor_sacar <= saldo:
                        conta["saldo"] = m.sacar(saldo, valor_sacar)
                        os.system('cls')
                        print("Valor sacado com sucesso!")
                        print(f"Seu novo saldo é: R$ {conta.get('saldo'):,.2f}\n")
                    else:
                        print("Saldo insuficiente!")
                    continue

                case "4":
                    os.system('cls')
                    valor_depositar = float(input("Informe o valor a ser depositado: R$ ").replace(",", "."))
                    conta["saldo"] = m.depositar(conta.get("saldo"), valor_depositar)
                    os.system('cls')
                    print(f"Valor depositado com sucesso!")
                    print(f"Seu novo saldo é: R$ {conta.get('saldo'):,.2f}\n")
                    continue

                case "5":
                    os.system('cls')
                    m.imprimir_dados_conta(conta)
                    continue
                
                case _:
                    os.system('cls')
                    print("Opcao invalida! Tente novamente.\n")
                    continue


    
    except Exception as e:
        print(f"Nao foi possivel cadastrar a conta bancaria. Erro: {e}")