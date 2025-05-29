import flet as ft


def main(page: ft.Page):
    page.title = "IMC Calculator" # adiciona o título da página na janela
    page.scroll = "adaptive" # adiciona a barra de rolagem caso a janela fique pequena
    page.theme_mode = ft.ThemeMode.LIGHT # define o tema da janela como claro

    def calcular_imc(e): # esse parametro "e" indica que a funcao receberá um evento como parâmetro

        if not peso.value:
            peso.error_text = "O campo Peso é obrigatório."
            page.update() # atualiza a página para refletir as mudanças
        else:
            peso.error_text = ""
            page.update() # atualiza a página para refletir as mudanças

        if not altura.value:
            altura.error_text = "O campo Altura é obrigatório."
            page.update() # atualiza a página para refletir as mudanças
        else:
            altura.error_text = ""
            peso.value = float(peso.value.replace(",", "."))  # substitui vírgula por ponto
            altura.value = float(altura.value.replace(",", ".")) # substitui vírgula por ponto

            if peso.value > 0 and altura.value > 0: # verifica se os valores de peso e altura são maiores que zero
                imc = peso.value / (altura.value ** 2)
                peso.value = ""  # limpa o campo de peso
                altura.value = ""  # limpa o campo de altura
                resultado.value = f"Seu IMC é: {imc:.2f}" # atribui o valor do IMC a variavel resultado
                page.update() # atualiza a página para refletir as mudanças
            elif peso.value <= 0 and altura.value > 0:
                peso.error_text = "Peso deve ser maior que zero."
                page.update()
            elif peso.value > 0 and altura.value <= 0:
                altura.error_text = "Altura deve ser maior que zero."
                page.update()
            else:
                peso.error_text = "Peso deve ser maior que zero."
                altura.error_text = "Altura deve ser maior que zero."
                page.update()
                
    peso = ft.TextField(
        label="Peso (kg): ", 
        suffix_text="kg",
        keyboard_type=ft.KeyboardType.NUMBER, # define o tipo de teclado como numérico
        )
    altura = ft.TextField(
        label="Altura (m): ", 
        suffix_text="m", 
        keyboard_type=ft.KeyboardType.NUMBER, # define o tipo de teclado como numérico
        on_submit=calcular_imc
        ) # o on_submit chama a função calcular_imc quando o usuário pressiona Enter
    botao_calcular = ft.ElevatedButton("Calcular IMC", on_click=calcular_imc) # o on_click chama a função calcular_imc quando o usuário clica no botão
    resultado = ft.Text(size=20, weight="bold") # cria um texto para exibir o resultado do IMC

    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text(
                        "\nIMC - Indice de Massa Corporal - Calcule o seu!", 
                        style=ft.TextThemeStyle.TITLE_LARGE
                        )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        peso, 
        altura,
        botao_calcular,
        resultado
    )


ft.app(main)
