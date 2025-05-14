
# declaracao de funcoes
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


# algoritimo principal
try:
    # entrada de dados
    base_informada = float(input("Informe a base do triangulo: ")).replace(",", ".")
    altura_informada = float(input("Informe a altura do triangulo: ")).replace(",", ".")

    # processamento
    area = calcular_area_triangulo(base_informada, altura_informada)

    # saida de dados
    print(f"A area do triangulo é: {area}")

except Exception as e:
    print(f"Nao foi possivel calculcar a area do triangulo. Erro: {e}")