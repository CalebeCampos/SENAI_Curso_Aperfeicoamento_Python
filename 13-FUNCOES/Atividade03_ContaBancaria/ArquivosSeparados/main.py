import contas as c
import menus as m
import os

if __name__ == "__main__":
    
    try:

        while True:
            m.menu_principal()
            opcao = input("Opcao desejada: ")

            match opcao:
                
                # CADASTRAR CONTA
                case "1": 
                    os.system('cls')
                    nome = input("Informe o nome do titular da conta: ").title()
                    cpf = input("Informe o CPF do titular da conta: ")
                    c.cadastrar_conta(nome, cpf)
                    continue
                
                # LISTAR CONTAS CADASTRADAS
                case "2": 
                    os.system('cls')
                    c.listar_contas()
                    continue 
                
                # ALTERAR TITULAR DA CONTA
                case "3": 
                    os.system('cls')
                    indice_conta_alterar = int(input("Informe a posicao da conta que deseja alterar: "))
                    if c.validar_conta(indice_conta_alterar):
                        c.imprimir_conta(indice_conta_alterar)
                        while True:
                            m.menu_alteracao_titular()
                            opcao_titular_escolhida = input("Opção desejada: ")
                            match opcao_titular_escolhida:                            
                                    case "1":                                     
                                        novo_titular_nome = input("Informe o nome do novo titular: ")
                                        c.alterar_nome_titular(indice_conta_alterar, novo_titular_nome)
                                        continue                                
                                    case "2":
                                        novo_titular_cpf = input("Informe o CPF do novo titular: ")
                                        c.alterar_cpf_titular(indice_conta_alterar, novo_titular_cpf)
                                        continue                                
                                    case "0":
                                        break
                                    case _:
                                        print("Opcao invalida!")
                                        print("\n")
                                        continue
                    else:
                        print("Conta nao encontrada!")
                    continue
                
                # EXCLUIR CONTA
                case "4": 
                    os.system('cls')
                    indice_conta_deletar = int(input("Informe a posicao da conta que deseja deletar: "))
                    if c.validar_conta(indice_conta_deletar) == True:
                        c.imprimir_conta(indice_conta_deletar)
                        c.excluir_conta(indice_conta_deletar)
                    else:
                        print("Conta nao encontrada!")
                    continue
                
                # SACAR
                case "5": 
                    os.system('cls')
                    indice_conta_sacar = int(input("Informe a posicao da conta que deseja sacar: "))
                    if c.validar_conta(indice_conta_sacar) == True:
                        c.imprimir_conta(indice_conta_sacar)                    
                        while True:
                            m.menu_saque()
                            opcao_saque_escolhido = input("Opção desejada: ")                  
                            match opcao_saque_escolhido:                                
                                case "1":  
                                    valor_saque = float(input("Valor a ser sacado: ").replace(",","."))
                                    c.sacar(indice_conta_sacar, valor_saque)
                                    continue                            
                                case "0":
                                    break                            
                                case _:
                                    print("Opcao invalida!")
                                    print("\n")
                                    continue
                    else:
                        print("Conta nao encontrada!")
                    continue

                case "6": # DEPOSITAR
                    os.system('cls')
                    indice_conta_depositar = int(input("Informe a posicao da conta que deseja depositar: "))
                    if c.validar_conta(indice_conta_depositar) == True:
                        c.imprimir_conta(indice_conta_depositar) 

                        while True:
                            m.menu_deposito()
                            opcao_deposito_escolhida = input("Opção desejada: ")
                            match opcao_deposito_escolhida:
                                case "1":
                                    valor_deposito = float(input("Informe o valor a ser depositado: ").replace(",","."))
                                    c.depositar(indice_conta_depositar, valor_deposito)
                                    continue
                                case "0":
                                    break
                                case _:
                                    print("Opcao invalida!\n")
                                    continue
                    else:
                        print("Conta nao encontrada!")                        
                    continue                           

                case "7": # CONSULTAR SALDO
                    os.system('cls')
                    indice_conta_consultar_saldo = int(input("Informe a posicao da conta que deseja consultar o saldo: "))
                    if c.validar_conta(indice_conta_consultar_saldo) == True:
                        c.imprimir_conta(indice_conta_consultar_saldo)
                        c.consultar_saldo(indice_conta_consultar_saldo)
                    else:
                        print("Conta nao encontrada!")
                    continue

                # SAIR
                case "0": 
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