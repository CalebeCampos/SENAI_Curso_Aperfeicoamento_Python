import math

# funcao usuando o recurso lambda
calcular_area_ciruclo = lambda r: math.pi * (r**2)

if __name__ == "__main__":
    try:
        r = float(input("Informe o raio do circulo: "))
        result = calcular_area_ciruclo(r)
        print(f"A area do circulo é: {result:,.2f}")
    except Exception as e:
        print(f"Nao foi possivel calcular a area do circulo. Erro: {e}")