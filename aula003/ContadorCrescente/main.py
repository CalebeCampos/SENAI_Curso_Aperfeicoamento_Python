# Tratamento de exceção
try:
    n = int(input("Informe um número inteiro positivo: "))

    # loop
    for i in range(n+1):
        print(i)

except Exception as e:
    print(f"Nao foi possivel realizar a contagem. Erro: {e}.")