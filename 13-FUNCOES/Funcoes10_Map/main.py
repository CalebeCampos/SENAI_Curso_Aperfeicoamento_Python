# funcao map
# pg - progressão geométrica

# declarando a função usando lambda
calcular_pg = lambda x: x * 2
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(calcular_pg, numeros))

print("Progressao Geométrica\n")
for numero in result:
    print(numero)

# def calcular_pg(x):
#     return x * 2
# resultado = list(map(calcular_pg, numeros))
# print("Progressao Geométrica\n")
# for numero in resultado:
#     print(numero)