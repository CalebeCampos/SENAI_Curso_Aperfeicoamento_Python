import flet as ft


def main(page: ft.Page):

    def mostrar_texto(event):
        texto_saida.value = f"Você digitou: {texto_entrada.value}"
        page.update()

    page.title = "Programacao orientada a eventos"
    page.theme_mode = ft.ThemeMode.LIGHT

    texto_entrada = ft.TextField(label="Informe seu nome: ", on_change=mostrar_texto)
    texto_saida = ft.Text()

    page.add(
        ft.SafeArea(
            ft.Text(
                "Programacao orientada a eventos",
                size=40,
                weight="bold"
            )
        ),
        texto_entrada,
        texto_saida
    )


ft.app(main)
