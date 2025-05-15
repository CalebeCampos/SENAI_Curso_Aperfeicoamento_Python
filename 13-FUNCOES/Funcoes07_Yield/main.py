import time
import modulo as m

# algoritimo principal
if __name__ == "__main__":

    nome_aluno = input("Digite o nome do aluno: ")
    resultado = m.verificar_matricula(nome_aluno)

    for verificacao in resultado:
        time.sleep(3)
        print(verificacao)