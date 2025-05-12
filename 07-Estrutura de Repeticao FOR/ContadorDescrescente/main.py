# Tratamento de exceção
try:
    n = int(input("Informe um número inteiro positivo: "))

    # loop
    for i in range(n, -1, -1): # o range vai n ate 0, e o -1 indica que o loop vai decrescer de 1 em 1
        # print(i) # imprime o valor de i
        print(i)

except Exception as e:
    print(f"Nao foi possivel realizar a contagem. Erro: {e}.")