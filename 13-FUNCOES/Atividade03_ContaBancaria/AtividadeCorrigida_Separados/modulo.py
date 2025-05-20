def depositar(saldo, valor):
    saldo += valor
    return saldo

def sacar(saldo, valor):
    saldo -= valor
    return saldo

def imprimir_dados_conta(titular):
    print(f"Nome: {titular.get('nome')}")
    print(f"CPF: {titular.get('cpf')}")
    print(f"Agência: {titular.get('agencia')}")
    print(f"Conta: {titular.get('conta')}")
    print(f"Saldo: R$ {titular.get('saldo'):,.2f}")