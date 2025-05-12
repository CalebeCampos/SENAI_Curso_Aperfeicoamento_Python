
pessoas = [
    {
        "nome": "Otavio",
        "idade": 18,
        "email": "otavio@gmail.com"
    },
    {
        "nome": "Flavio",
        "idade": 25,
        "email": "flavio@gmail.com"
    },
    {
        "nome": "Sandra",
        "idade": 33,
        "email": "sandra@gmail.com"
    }
]

# imprimindo a lista de dicionarios
print(pessoas)

# imprimindo os elementos da lista
for pessoa in pessoas:
    print(pessoa)

# imprimindo os elementos de cada dicionario dos elementos da lista
for pessoa in pessoas:
    print(f"\n{'-'*20}\n")
    for chave in pessoa:
        print(f"{chave.title()}: {pessoa.get(chave)}")