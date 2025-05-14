
# funcao com parametros e sem retorno
def dar_boas_vindas(nome):
    print(f"{'='*20} CURSO DE APERFEIÇOAMENTO PYTHON {'='*20}\n")
    print(f"Seja bem vindo(a) {nome}!")

# executando a funcao
nome_informado = input("Informe seu nome: ")
dar_boas_vindas(nome_informado)