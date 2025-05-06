import os

dados = {
    'nome': 'Lucas',
    'idade': 25,
    'cpf': '123.456.789-00'
}

for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}")
print("\n")

# inserindo nova chave e valor no dicionario
dados['email'] = input("Digite o email do usuario: ")

os.system('cls')

for chave in dados:
    print(f"{chave.title()}: {dados.get(chave)}")
print("\n")

