# importar modulo
# import funcoes as fun
from funcoes import calcular_area_quadrilatero, calcular_area_triangulo # importa apenas as funcoes que deseja do modulo funcoes


if __name__ == "__main__": # esse trecho de codigo indica que este arquivo é o principal e nao podera ser importado por outros arquivos

    try:
        
        print("Escolha a figura da qual deseja calcular a area:\n")
        print("1 - Triangulo")
        print("2 - Quadrilatero")
        opcao_informada = int(input("Opcao desejada: "))

        if opcao_informada == 1 or opcao_informada == 2:
            b = float(input("Informe o valor da base: ").replace(",", "."))
            h = float(input("Informe o valor da altura: ").replace(",", "."))
            match opcao_informada:
                case 1:
                    # area_do_triangulo = fun.calcular_area_triangulo(b, h)
                    area_do_triangulo = calcular_area_triangulo(b, h)
                    print(f"A area do triangulo é: {area_do_triangulo:.2f}")
                case 2:
                    # area_do_quadrilatero = fun.calcular_area_quadrilatero(b, h)
                    area_do_quadrilatero = calcular_area_quadrilatero(b, h)
                    print(f"A area do quadrilatero é: {area_do_quadrilatero:.2f}")
        else:
            print("Opcao invalida.")
    
    except Exception as e:
        print(f"Nao foi possivel executar a operacao. Erro: {e}")
