nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# IF e ELSE de forma ternaria
maioridade = "MAIOR" if idade >= 18 else "MENOR"
print(f"Olá {nome}, você é {maioridade} de idade.")