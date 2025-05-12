nomes = []

try:
   
    while True:
        item = input("Digite um nome ou deixe em branco para exibir a lista: ")
        if item != "":
            nomes.append(item)
            continue
        else:
            break
       
    nomes.sort() # ordenando a lista de nomes em ordem alfabética   
   
except Exception as e:
    print(f"Erro: {e}")

finally:
    
    for item in nomes:
        print(item)
