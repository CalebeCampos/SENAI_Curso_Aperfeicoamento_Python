import os

lista_compra = []

try:
   
    while True:
        item = input("Digite os itens da sua lista de compras ou deixe em branco para exibir a lista: ")
        os.system("cls") # Limpa o terminal
        if item != "":
            lista_compra.append(item)
            print(f"{item}, inserido na lista de compras com sucesso!")
            continue
        else:
            break
       
    lista_compra.sort() # ordenando a lista de nomes em ordem alfabética   
   
except Exception as e:
    print(f"Erro: {e}")

finally:

    if len(lista_compra) == 0:
        print("Lista de compras vazia!")
    else:
        print("Lista de compras:\n")
        for n in range(len(lista_compra)):
            print(f"Item {n+1}: {lista_compra[n]}")
