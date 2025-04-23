listaCompras = []

try:
   
    while True:
        item = input("Digite os itens da sua lista de compras ou deixe em branco para exibir a lista: ")
        if item != "":
            listaCompras.append(item)
            continue
        else:
            break
       
    listaCompras.sort() # ordenando a lista de nomes em ordem alfabética   
   
except Exception as e:
    print(f"Erro: {e}")

finally:
    
    for n in range(len(listaCompras)):
        print(f"Item {n+1}: {listaCompras[n]}")
