import os

lista_cidades = [
    "São Paulo", "Rio De Janeiro", 
    "Belo Horizonte", "Salvador", 
    "Fortaleza", "Curitiba", "Recife", 
    "Porto Alegre", "Brasília", 
    "Manaus", "Goiânia", "Maceió"]

try:
   
    while True:
        
        for i in range(len(lista_cidades)):
            print(f"Cidade de codigo {i}: {lista_cidades[i]}")

        deseja_alterar = input("Deseja alterar alguma cidade? (s/n): ").lower()

        match deseja_alterar:
            case "s":
                codigo_cidade_informada = int(input("Digite o codigo da cidade que deseja altear: "))
                nova_cidade_informada = input("Digite o nome da nova cidade: ").title()
                lista_cidades[codigo_cidade_informada] = nova_cidade_informada
                os.system("cls")  # limpa a tela do terminal
                continue
            case "n":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break

except Exception as e:
    print(f"Erro: {e}")

