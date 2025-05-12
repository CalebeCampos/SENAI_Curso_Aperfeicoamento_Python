# Tratamento de exceção
try:
    n = int(input("Informe um número inteiro positivo: "))

    # loop
    while n >= 0:
        print(n)
        n -= 1

except Exception as e:
    print(f"Você não digitou um número inteiro positivo. Erro: {e}.")