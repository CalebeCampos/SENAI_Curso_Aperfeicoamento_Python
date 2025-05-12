
try:

    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    while True:

        print(f"{'-'*20}LISTA DE FILMES{'-'*20}\n")
        print("1 - Sala 01 - Matrix (18 anos)")
        print("2 - Sala 02 - Vingadores (12 anos)")
        print("3 - Sala 03 - Toy Story (Livre)")
        print("4 - Sala 04 - O Rei Leão (Livre)")
        print("5 - Sala 05 - Star Wars (10 anos)")

        filme = int(input("Informe o filme desejado: "))

        match filme:
            case 1:
                if idade < 18:
                    print(f"{nome} você não pode assistir este filme, a idade mínima é 18 anos.")
                else:
                    print("Boa secao!")
                    break
            case 2:
                if idade < 12:
                    print(f"{nome} você não pode assistir este filme, a idade mínima é 12 anos.")
                else:
                    print("Boa secao!")
                    break
            case 3:
                print("Boa secao!")
                break
            case 4:
                print("Boa secao!")
                break
            case 5:
                if idade < 10:
                    print(f"{nome} você não pode assistir este filme, a idade mínima é 10 anos.")
                else:
                    print("Boa secao!")
                    break
            case _:
                print("Filme inválido.")
        
        continuar = input("Deseja escolher outro filme? (s/n): ").lower()

        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue

except Exception as e:
    print(f"{nome} voce informou uma idade invalida! Erro: {e}.")

finally:
    print("Programa encerrado.")