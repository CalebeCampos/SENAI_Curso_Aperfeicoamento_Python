"""
Atividade: crie um programa que calcule a sequencia fibonacci até a quantidade informada pelo usuario
obs: F(n) = F(n-1) + F(n-2)
"""
import os

# declaracao de funcao recursiva
def calcular_termo_fibonacci(n):
    return n if n <= 1 else (calcular_termo_fibonacci(n-1) + calcular_termo_fibonacci(n-2))        
        
def gerar_sequencia_fibonacci(quantidade_termos):
    sequencia = []
    for i in range(1, quantidade_termos+1):
        termo_gerado = calcular_termo_fibonacci(i)
        sequencia.append(termo_gerado)
    return sequencia

if __name__ == "__main__":
    try:
        
        while True:
            
            qtd = int(input("Informe a quantidade de algarismos voce deseja ver da sequencia de Fibonacci ou 0 para sair: "))
            
            if qtd> 0:
                os.system('cls')
                sequencia_fibonacci = gerar_sequencia_fibonacci(qtd)
                print(sequencia_fibonacci)
                continue
            else:
                print("Programa finalizado!")
                break

    except Exception as e:
        print(f"Nao foi possivel calcular a seguencia de fibonacci. Erro: {e}")