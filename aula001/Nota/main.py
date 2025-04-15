nome = input("Digite seu nome: ")
nota = float(input("Digite sua nota: "))

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"Olá {nome}, você foi APROVADO com a nota {nota}.")
    elif nota >= 5:
        print(f"Olá {nome}, você está em RECUPERAÇÃO com a nota {nota}.")
    else:
        print(f"Olá {nome}, você foi REPROVADO com a nota {nota}.")
else:
    print(f"Olá {nome}, a nota {nota} é inválida. A nota deve ser entre 0 e 10.")