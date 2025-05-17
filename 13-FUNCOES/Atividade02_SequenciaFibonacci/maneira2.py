import os

# declaracao de funcao
def calcular_fibonacci(n):
    return n if n <= 1 else calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

if __name__ == "__main__":
    try:
        while True:
            
            n = int(input("Informe a quantidade de algarismos voce deseja ver da sequencia de Fibonacci ou 0 para sair: "))

            if n > 0:
                os.system('cls')
                for i in range(1, n+1):
                    print(calcular_fibonacci(i))
                continue
            else:
                print("Programa finalizado!")
                break         
        
    except Exception as e:
        print(f"Nao foi possivel calcular a sequencia de Fibonacci. Erro: {e}")