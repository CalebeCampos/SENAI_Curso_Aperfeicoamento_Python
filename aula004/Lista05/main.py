nomes = ["Maria de Fátima", "Lucas Ramos", "Ana Clara", "João Carvalho", "Pedro Souza"]

# ordenando a lista de nomes em ordem alfabética
nomes.sort()

# imprimindo os elementos da lista na ordem alfabetica
for n in range(len(nomes)):
    print(f"{n+1}: {nomes[n]}")