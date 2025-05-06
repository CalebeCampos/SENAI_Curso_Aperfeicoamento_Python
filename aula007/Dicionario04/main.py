import os

dados = {
    'nome': 'Lucas',
    'idade': 25,
    'cpf': '123.456.789-00'
}



try:

    while True:

        os.system('cls')
        
        for chave in dados:
            print(f"{chave.title()}: {dados.get(chave)}")
        print("\n")

        prosseguir = input("Deseja inserir novos dados? (s/n): ").lower()

        match prosseguir:
            case 's':
                # inserindo nova chave e valor no dicionario
                nova_chave = input("Digite o nome da nova chave: ")
                valor_nova_chave = input(f"Digite o valor da nova chave {nova_chave}: ")
                dados[nova_chave] = valor_nova_chave
                os.system('cls')
                continue
            case 'n':
                break
            case _:
                print("Opcao invalida!")
                continue




except Exception as e:
    print(f"Nao foi possivel inserir a nova chave. Erro: {e}")