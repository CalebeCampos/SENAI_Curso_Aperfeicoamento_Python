# importando a biblioteca time
import time
import os

# Tratamento de exceção
try:
    n = int(input("Informe um número inteiro positivo: "))

    # loop
    for i in range(n, -1, -1): 
        os.system("cls") # Limpa o terminal
        print(f"{i}...") # Imprime o número atual da contagem regressiva
        time.sleep(1) # Define o tempo de espera entre os números
    print("Explodiu!")

except Exception as e:
    print(f"Nao foi possivel realizar a contagem regressiva. Erro: {e}.")