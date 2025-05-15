'''
crie um programa onde o usuario podera escolher se deseja calcular a equacao do 1º grau ou a equacao do 2º, e o programa retorna o resultado da equacao.
obs: o programa deverá ser executado em loop
'''
import os
import math

#definicao de funcoes
def calcular_equacao_primeiro_grau(a, b):
    x = -b/a
    return x

def calcular_equacao_segundo_grau(a, b, c):
    delta = b**2-(4*a*c)
    if delta<0:
        yield "Não há valores reais de x que satisfaçam a equação"
    elif delta>0:
        x_linha = (-b+math.sqrt(delta))/2*a
        x_duas_linhas = (-b-math.sqrt(delta))/2*a
        yield x_linha
        yield x_duas_linhas
    else: #delta == 0:
        x_linha = -b/2*a
        yield x_linha
        
try:

    while True:

        print("Informe uma opção...")
        print("1 - para equacao do 1º grau")
        print("2 - para equacao do 2º grau")
        print("0 - para sair")

        opcao = int(input("Opção desejada: "))
        
        match opcao:
            case 1:
                os.system('cls')
                a = float(input('Informe o valor de "a": ').replace(",","."))
                b = float(input('Informe o valor de "b": ').replace(",","."))
                resultado_equacao_primeiro_grau = calcular_equacao_primeiro_grau(a, b)
                print(f'O valor de "x" é: {resultado_equacao_primeiro_grau}')
                print("\n")
                continue
            case 2:
                os.system('cls')
                a = float(input('Informe o valor de "a": ').replace(",","."))
                b = float(input('Informe o valor de "b": ').replace(",","."))
                c = float(input('Informe o valor de "c": ').replace(",","."))
                resultado_equacao_segundo_grau = calcular_equacao_segundo_grau(a, b, c)
                for resultados in resultado_equacao_segundo_grau:
                    print(f'O valor de "x" é: {resultados}')
                print("\n")
                continue
            case _:
                os.system('cls')
                print("Programa finalizado!")
                break

except Exception as e:
    print(f"Nao foi possivel realizar o calculo. Erro: {e}")