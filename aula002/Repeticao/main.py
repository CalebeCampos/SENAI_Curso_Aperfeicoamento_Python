try:

    while True:

        nome = input("Informe seu nome: ")
        idade = int(input("Informe sua idade: "))

        print(nome,", voce é menor de idade." if idade < 18 else ", voce é maior de idade.")

        continuar = input("Deseja informar novos dados? (s/n): ").lower()
        match continuar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")
                continue
        
except Exception as e:
    print(f"Idade invalida. Erro: {e}.")

finally:
    print("Programa encerrado.")