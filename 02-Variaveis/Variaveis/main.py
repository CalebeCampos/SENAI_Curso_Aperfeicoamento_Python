# operador de comentario, comenta uma linha
'''
3 aspas simples, abre e fecha um bloco de texto.
operador de comentario, 
comenta um bloco de linhas .
'''
"""
3 aspas duplas, abre e fecha um bloco de texto.
operador de comentario,
comenta um bloco de linhas.
"""


texto = "Olá, Mundo!" # variável texto recebe o valor "Olá, Mundo!"

print(texto)  # imprime o valor da variável texto


nome_usuario = "Calebe Campos"
idade_usuario = 35
altura_usuario = 1.75
peso_usuario = 70.5
is_programador = True

# Concatenação de strings, dentro da funcao print()....
print("Nome:", nome_usuario)  # imprime o nome do usuário
print("Idade:", idade_usuario)  # imprime a idade do usuário
print("Altura:", altura_usuario)  # imprime a altura do usuário
print("Peso:", peso_usuario)  # imprime o peso do usuário
print("É programador?", is_programador)  # imprime se o usuário é programador ou não

# Concatenação de strings, dentro da funcao print() utilizando f-string
# f-string é uma forma de formatar strings em Python, permitindo incluir variáveis diretamente na string
# essa forma de formatação é mais legível e fácil de entender, porem nao dá pra usar quebra de linha
print(f"Nome: {nome_usuario}, Idade: {idade_usuario}, Altura: {altura_usuario}, Peso: {peso_usuario}, É programador? {is_programador}")  # imprime todas as informações do usuário em uma única linha

# Concatenação de strings, dentro da funcao print() utilizando .format()
# o .format() é um método de formatação de strings que permite inserir valores em uma string usando chaves {} como marcadores de posição
# essa forma de formatação é mais legível e fácil de entender, porem nao dá pra usar quebra de linha
print("Nome: {}, Idade: {}, Altura: {}, Peso: {}, É programador? {}".format(nome_usuario, idade_usuario, altura_usuario, peso_usuario, is_programador))  # imprime todas as informações do usuário em uma única linha

# Concatenação de strings, dentro da funcao print() utilizando %
# o % é um operador de formatação de strings que permite inserir valores em uma string usando %s como marcador de posição
# essa forma de formatação é mais legível e fácil de entender, porem nao dá pra usar quebra de linha
print("Nome: %s, Idade: %d, Altura: %.2f, Peso: %.2f, É programador? %s" % (nome_usuario, idade_usuario, altura_usuario, peso_usuario, is_programador))  # imprime todas as informações do usuário em uma única linha

# Concatenação de strings, dentro da funcao print() utilizando + e str()
# o + é um operador de concatenação de strings que permite unir duas ou mais strings em uma única string
# o str() é uma função que converte um valor em uma string
# essa forma de formatação é mais legível e fácil de entender
print("Nome: " + nome_usuario)
print("Idade: " + str(idade_usuario))
print("Altura: " + str(altura_usuario))
print("Peso: " + str(peso_usuario))
print("É programador? " + str(is_programador))

# exibe o tipo da variável, dentro da funcao print() utilizando type()
print(type(nome_usuario))  # imprime o tipo da variável nome_usuario
print(type(idade_usuario))  # imprime o tipo da variável idade_usuario
print(type(altura_usuario))  # imprime o tipo da variável altura_usuario
print(type(peso_usuario))  # imprime o tipo da variável peso_usuario
print(type(is_programador))  # imprime o tipo da variável is_programador

