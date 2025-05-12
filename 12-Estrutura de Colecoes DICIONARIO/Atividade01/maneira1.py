import os

usuario = {}

try:

    usuario["Nome"] = input("Informe o nome: ")
    usuario["Data Nascimento"] = input("Informe a data de nascimento: ")
    usuario["CPF"] = input("Informe o CPF: ")
    usuario["email"] = input("Informe o email: ")
    usuario["Genero"] = input("Informe o genero: ")
    usuario["Telefone"] = input("Informe o telefone: ")
    usuario["Altura"] = float(input("Informe a altura em metros: ").replace(",","."))
    usuario["Peso"] = float(input("Informe o peso em kg: ").replace(",","."))
    usuario["Tipo sanguineo"] = input("Informe o tipo sanguineo: ")

    os.system("cls")

    for interator in usuario:
        print(f"{interator.title()}: {usuario.get(interator)}")

    imc = usuario.get("Peso")/usuario.get("Altura")**2
    print(f"{usuario.get("Nome")} seu IMC é: {imc:,.2f}")

    if imc < 18.5:
        print(f"{usuario.get("Nome")} está abaixo do peso.")
    elif imc < 25:
        print(f"{usuario.get("Nome")} está no peso ideal.")
    elif imc < 30:
        print(f"{usuario.get("Nome")} está acima do peso.")
    elif imc < 35:
        print(f"{usuario.get("Nome")} está obeso.")
    elif imc < 40:
        print(f"{usuario.get("Nome")} está com obesidade nivel II.")
    else:
        print(f"{usuario.get("Nome")} está com obesidade morbida.")

except Exception as e:
    print(f"Nao foi possivel inserir os dados. Erro: {e}")