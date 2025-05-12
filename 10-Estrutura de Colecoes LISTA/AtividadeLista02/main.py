import os

notas = []

try:
    
    while True:
        nota = float(input("Digite a nota do aluno: ").replace(",", "."))
        
        if nota >= 0 and nota <= 10:
            notas.append(nota)
            print("Nota inserida com sucesso!")

            while True:
                continuar = input("Deseja inserir mais notas? (s/n): ").strip().lower()
                if continuar =='s' or continuar == 'n':
                    os.system('cls') #limpa a tela do terminal
                    break
                else:
                    print("Opção inválida.")
                    continue
            
            match continuar:
                case 's':
                    continue
                case 'n':
                    break

        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")
            continue

    for i in range(len(notas)):
        print(f"Nota {i+1}: {notas[i]}")

    media = sum(notas) / len(notas)
    media = round(media, 2)     

except Exception as e:
    print(f"Nao foi possivel inserir as notas e calcular a media. Erro: {e}")

finally:
    # print(f"\nA media das notas é: {media}")
    # print(f"\nA media das notas é: {media:,.2f}") #imprime o valor da media com 2 casas decimais
    print("\n")
    # print(f"A media das notas é: {media:,.2f}") #imprime o valor da media com 2 casas decimais
    print(f"A media das notas é: {media}")

    if media >= 7:
        print("O aluno está aprovado!")
    elif media >= 5:
        print("O aluno está de recuperação!")
    else:
        print("O aluno está reprovado!")
