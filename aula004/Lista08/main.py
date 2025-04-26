import os

cidades = [
    "São Paulo", "Rio De Janeiro", 
    "Belo Horizonte", "Salvador", 
    "Fortaleza", "Curitiba", "Recife", 
    "Porto Alegre", "Brasília", 
    "Manaus", "Recife", "Goiânia", 
    "Recife", "Maceió", "Fortaleza"]

try:

    while True:

        os.system("cls") # limpa a tela do terminal

        cidade_informada = input("Digite o nome de uma cidade: ").title()

        quantidade_valores_encontrados = cidades.count(cidade_informada)

        if quantidade_valores_encontrados != 0:
            print(f"A cidade {cidade_informada} foi encontrada {quantidade_valores_encontrados} vezes.")
        else:
            print(f"A cidade {cidade_informada} não foi encontrada na lista.")

        continuar = input("Deseja continuar? (s/n): ").lower()
        match continuar:
            case "s":
                continue
            case "n":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break

except Exception as e:
    print(f"Erro: {e}")
