import flet as ft


def main(page: ft.Page):
    page.title = "Example Hello World em FLET"
    page.add(
        ft.SafeArea(
            ft.Text("Olá, Mundo!", size=30, color="blue", weight="bold")
        )
    )

ft.app(target=main)
