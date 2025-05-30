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

                if   imc < 18.5:
                    diagnostico.value = "Você está abaixo do peso!"
                    diagnostico.color = ft.Colors.BLUE # muda a cor do texto para vermelho se o IMC for menor que 18.5
                elif imc < 25:
                    diagnostico.value = "Você está com peso normal!"
                    diagnostico.color = ft.Colors.GREEN # muda a cor do texto para verde se o IMC for menor que 25
                elif imc < 30:
                    diagnostico.value = "Você está com sobrepeso!"
                    diagnostico.color = ft.Colors.YELLOW # muda a cor do texto para vermelho se o IMC for maior que 25
                elif imc < 35:
                    diagnostico.value = "Você está com obesidade!"
                    diagnostico.color = ft.Colors.ORANGE # muda a cor do texto para vermelho se o IMC for maior que 30
                elif imc < 40:
                    diagnostico.value = "Você está com obesidade severa!"
                    diagnostico.color = ft.Colors.RED # muda a cor do texto para vermelho se o IMC for maior que 35
                else:
                    diagnostico.value = "Você está com obesidade mórbida!"
                    diagnostico.color = ft.Colors.PURPLE # muda a cor do texto para vermelho se o IMC for maior que 40
                
                diagnostico.update() # atualiza o texto do diagnóstico
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

    # Declaracao das variaveis           
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
    diagnostico = ft.Text(size=15, weight="bold") # cria um texto para exibir o diagnóstico do IMC

    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text(
                        "\nIMC - Indice de Massa Corporal - Calcule o seu!", 
                        style=ft.TextThemeStyle.TITLE_LARGE,
                        weight="bold",
                        size=30                        
                        )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        peso, 
        altura,
        botao_calcular,
        resultado,
        diagnostico
    )


ft.app(main)
