# tratamento de exceção
# o try é para tentar executar o código, se der erro, ele vai para o except
# e executa o que está dentro do except
# o finally é para executar algo independente do que acontecer, se der erro ou não

try:
    # tenta executar o código
    x = int(input("Informe um numero inteiro: "))

    print(f"Você digitou o número {x}.")

except Exception as e:
    # se der erro, ele executa o que está dentro do except
    print(f"Você não digitou um número inteiro. Erro: {e}.")

finally:
    # executa o que está dentro do finally, independente do que acontecer, dao erro ou não no try
    print("Fim do programa.")