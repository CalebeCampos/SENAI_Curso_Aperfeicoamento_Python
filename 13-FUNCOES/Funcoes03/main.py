
# funcao com parametros e com retorno
def dar_boas_vindas(nome_aluno, nome_curso):
    return f"{nome_aluno}, seja bem vindo ao curso de {nome_curso}!"

# executando a funcao
nome_aluno = input("Informe seu nome: ")
nome_curso = input("Informe o nome do curso: ")
mensagem = dar_boas_vindas(nome_aluno, nome_curso)
print(mensagem)
