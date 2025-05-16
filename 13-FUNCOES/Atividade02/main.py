"""
Atividade: crie um programa que calcule a sequencia fibonacci até a quantidade informada pelo usuario
"""


# declaracao de funcao recursiva
def calcular_sequencia_fibonacci(n):
    return n * calcular_sequencia_fibonacci(n-1)
        


if __name__ == "__main__":
    try:
        qtd = int(input("Informe a quantidade de algarismos voce deseja ver da sequencia de Fibonacci: "))



    except Exception as e:
        print(f"Nao foi possivel calcular a seguencia de fibonacci. Erro: {e}")