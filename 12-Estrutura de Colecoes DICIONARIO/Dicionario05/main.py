

chaves = ('Nome', 'Idade', 'Sexo', 'Altura', 'Peso', 'Nacionalidade')

usuario = {
    chaves[0]: 'Lucas',
    chaves[1]: 25,
    chaves[2]: 'Masculino',
    chaves[3]: 1.75,
    chaves[4]: 70.0,
    chaves[5]: 'Brasileiro'
}

for chave in usuario:
    print(f"{chave.title()}: {usuario.get(chave)}")