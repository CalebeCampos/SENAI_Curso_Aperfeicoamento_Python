import math

# funcao simples sem o uso do recurso lambda
def calcular_area_ciruclo(r):
    area = math.pi * (r**2)
    return area

if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do circulo: "))
        result = calcular_area_ciruclo(r)
        print(f"A area do circulo é: {result:,.2f}")
    except Exception as e:
        print(f"Nao foi possivel calcular a area do circulo. Erro: {e}")