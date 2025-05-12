
try:

    nome = input("Informe seu nome: ")
    idade = int(input("Informe sua idade: "))

    while True:

        print(f"{'-'*20}LISTA DE FILMES{'-'*20}\n")
        print("Escolha um filme para assistir:")
        print("1 - Sala 01 - Matrix (18 anos)")
        print("2 - Sala 02 - Vingadores (12 anos)")
        print("3 - Sala 03 - Toy Story (Livre)")
        print("4 - Sala 04 - O Rei Leão (Livre)")
        print("5 - Sala 05 - Star Wars (10 anos)")

        filme = int(input("Informe o filme desejado: "))

        match filme:
            case 1:
                idade_minima = 18
            case 2:
                idade_minima = 12
            case 3:
                idade_minima = 0
            case 4:
                idade_minima = 0
            case 5:
                idade_minima = 10
            case _:
                idade_minima = idade+1
        
        if idade >= idade_minima:
            print("Boa secao!")
            break
        else:
            print(f"{nome} você não pode assistir este filme.")
            print(f"A idade mínima para este filme é: {idade_minima}")
            print("Escolha outro filme!")
            continue

except Exception as e:
    print(f"{nome} voce informou uma idade invalida! Erro: {e}.")

finally:
    print("Programa encerrado.")