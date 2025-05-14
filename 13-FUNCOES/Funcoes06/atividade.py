# importar modulo
import funcoes as fun

if __name__ == "__main__": # esse trecho de codigo indica que este arquivo é o principal e nao podera ser importado por outros arquivos

    try:
        
        print("Escolha a figura da qual deseja calcular a area:\n")
        print("1 - Triangulo")
        print("2 - Quadrilatero")
        print("3 - Trapezio")
        opcao_informada = int(input("Opcao desejada: "))
        h = float(input("Informe o valor da altura: ").replace(",", "."))

        if opcao_informada == 1 or opcao_informada == 2:
            b = float(input("Informe o valor da base: ").replace(",", "."))
            match opcao_informada:
                case 1:
                    area_do_triangulo = fun.calcular_area_triangulo(b, h)
                    print(f"A area do triangulo é: {area_do_triangulo:.2f}")
                case 2:
                    area_do_quadrilatero = fun.calcular_area_quadrilatero(b, h)
                    print(f"A area do quadrilatero é: {area_do_quadrilatero:.2f}")
        elif opcao_informada == 3:
            b_maior = float(input("Informe o valor da base maior: ").replace(",", "."))
            b_menor = float(input("Informe o valor da base menor: ").replace(",", "."))
            area_do_trapezio = fun.calcular_area_trapezio(b_maior, b_menor, h)
            print(f"A area do trapezio é: {area_do_trapezio:.2f}")
        else:
            print("Opcao invalida.")
    
    except Exception as e:
        print(f"Nao foi possivel executar a operacao. Erro: {e}")
