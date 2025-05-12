import os

chaves = ('Nome', 'Idade', 'Sexo', 'Altura', 'Peso', 'Nacionalidade')

usuario = {
    chaves[0]: 'Lucas',
    chaves[1]: 25,
    chaves[2]: 'Masculino',
    chaves[3]: 1.75,
    chaves[4]: 70.0,
    chaves[5]: 'Brasileiro'
}

try:

    while True:
        
        for chave in usuario:
            print(f"{chave.title()}: {usuario.get(chave)}")
        print("\n")

        prosseguir = input("Deseja atualizar algum dado? (s/n): ").strip().lower()

        match prosseguir:
            case 's':
                chave_informada = input("Informe o nome da chave que deseja atualizar: ").strip().title()
                if chave_informada in chaves:
                    novo_valor_informado = input(f"Informe o novo valor para {chave_informada}: ").strip()
                    usuario[chave_informada] = novo_valor_informado
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    print(f"A chave {chave_informada.title()} nao existe!")
                    print("\n")
                    continue
            case 'n':
                break
            case _:
                print("Opção inválida!")
                continue

except Exception as e:
    print(f"Nao foi possivel atualizar os dados. Erro: {e}")