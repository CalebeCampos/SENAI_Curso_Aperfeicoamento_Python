import flet as ft
import random

def main(page: ft.Page):

    # Configurações da página
    page.title = "Sortear nome"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    lista_nomes = []  # Lista de nomes

    # Elementos da interface
    nome = ft.TextField(label="Informe um nome: ", on_submit=lambda e: inserir_nome())
    botao_inserir_nome = ft.ElevatedButton("INSERIR", on_click=lambda e: inserir_nome())
    botao_sortear_nome = ft.ElevatedButton("SORTEAR", on_click=lambda e: sortear_nome())
    mensagem_nome_inserido = ft.Text(size=20, weight="bold", color=ft.Colors.BLACK)
    mensagem_lista_vazia = ft.Text(size=20, weight="bold", color=ft.Colors.RED)
    texto_nome_sorteado = ft.Text("", size=25, weight="bold", color=ft.Colors.GREEN)

    # Container da lista de nomes exibidos
    lista_exibida = ft.Column()

    def atualizar_lista_exibida():
        lista_exibida.controls.clear()
        for i, n in enumerate(lista_nomes, start=1):
            lista_exibida.controls.append(ft.Text(f"{i}. {n}", size=15, weight="bold"))
        page.update()

    def inserir_nome():
        if not nome.value:
            nome.error_text = "É necessário informar um nome."
            mensagem_nome_inserido.value = ""
            mensagem_lista_vazia.value = ""
        else:
            nome.error_text = ""
            lista_nomes.append(nome.value)
            mensagem_nome_inserido.value = "Nome gravado com sucesso!"
            mensagem_lista_vazia.value = ""
            nome.value = ""
            atualizar_lista_exibida()  # Atualiza a exibição da lista
        page.update()

    def sortear_nome():
        if not lista_nomes:
            mensagem_lista_vazia.value = "Nenhum nome cadastrado para sortear."
            mensagem_nome_inserido.value = ""
            texto_nome_sorteado.value = ""  # Limpa o nome sorteado anterior, se houver
        else:
            mensagem_lista_vazia.value = ""
            mensagem_nome_inserido.value = ""
            texto_nome_sorteado.value = f"{random.choice(lista_nomes)}"
        page.update()

    # Layout da interface
    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text(
                    "\nSORTEIO DE NOMES",
                    color=ft.Colors.BLUE,
                    text_align=ft.TextAlign.CENTER,
                    style=ft.TextThemeStyle.TITLE_LARGE,
                    weight="bold",
                    size=30
                )],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        nome,
        ft.Row(
            [botao_inserir_nome, ft.Text("  "), botao_sortear_nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        mensagem_nome_inserido,
        mensagem_lista_vazia,
        ft.Text("Lista de nomes:", size=20, weight="bold", color=ft.Colors.BLACK),
        lista_exibida,  # Aqui é onde a lista será exibida
        ft.Text("Nome sorteado:", size=20, weight="bold", color=ft.Colors.BLACK),
        texto_nome_sorteado  # Exibição fixa do nome sorteado
    )

ft.app(main)
