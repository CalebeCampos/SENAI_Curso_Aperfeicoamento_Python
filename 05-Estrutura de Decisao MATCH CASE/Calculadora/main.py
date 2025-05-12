x = float(input("Informe o valor de x: "))
y = float(input("Informe o valor de y: "))

# apresenta as opçoes de operacoes para escolha do usuario
print("Escolha a operacao desejada: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Resto da Divisão")

operador = int(input("Informe a operação desejada: "))

# estrutura do match case para realizar a operação escolhida pelo usuário, exatamente como o switch case das outras linguagens
match operador:
    case 1:
        print(f"O resultado da soma é: {x+y}.")
    case 2:
        resultado = x - y
        print(f"O resultado da subtração é: {x-y}.")
    case 3:
        print(f"O resultado da multiplicação é: {x*y}.")
    case 4:
        print(f"O resultado da divisão é: {x/y}.")
    case 5:
        print(f"O resultado do resto da divisão é: {x%y}.")
    # o case _ é o padrão, ou seja, se nenhuma das opções acima for escolhida, ele executa o que está dentro do case _
    case _:
        print("Operação inválida.")