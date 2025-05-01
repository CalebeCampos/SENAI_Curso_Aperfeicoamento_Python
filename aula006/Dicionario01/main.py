# declaracao de dicionario

usuario = {
    'nome': "Lucas",
    'idade': 25,
    'profissao': "Programador"
}


# imprimindo as chaves do dicionario
print("imprimindo as chaves do dicionario")
for chave in usuario:
    print(chave)

print("\n")

# imprimindo os valores do dicionario
print("imprimindo os valores do dicionario")
for dado in usuario:
    print(usuario[dado])

print("\n")

# imprimindo os valores de cada chave do dicionario OPCAO 1
print("imprimindo os valores de cada chave do dicionario")
print(usuario['nome'])
print(usuario['idade'])
print(usuario['profissao'])

print("\n")

# imprimindo os valores de cada chave do dicionario OPCAO 2
print("imprimindo os valores de cada chave do dicionario")
print(usuario.get('nome'))
print(usuario.get('idade'))
print(usuario.get('profissao'))
print(usuario.get('endereco')) # tentando imprimir um valor que não existe a chave no dicionario, retorna None


print("\n")

# imprimindo os valores de cada chave do dicionario OPCAO 3
print("imprimindo os valores de cada chave do dicionario")
print(usuario.items()) # retorna uma lista de tuplas com as chaves e valores do dicionario
print(usuario.keys()) # retorna uma lista com as chaves do dicionario
print(usuario.values()) # retorna uma lista com os valores do dicionario