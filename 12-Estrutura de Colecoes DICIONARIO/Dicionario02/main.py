# outra forma de declarar dicionario
# dicionario = dict(chave1=valor1, chave2=valor2, chave3=valor3)
usuario = dict(nome="Lucas", idade=25, profissao="Programador")

# imprimindo o valor de cada chave do dicionario pelo chave
for chave in usuario:
    print(f"{chave.title()}: {usuario[chave]}")

# imprimindo o valor de cada chave do dicionario pela funcao get passando a chave
for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")