import flet as ft
import random  # importa o módulo random para gerar números aleatórios


def main(page: ft.Page):
    
    #configuracoes da pagina
    page.title = "Sortear nome" # adiciona o título da página na janela
    page.scroll = "adaptive" # adiciona a barra de rolagem caso a janela fique pequena
    page.theme_mode = ft.ThemeMode.LIGHT # define o tema da janela como claro
        
    def inserir_nome(e):
        if not nome.value:
            nome.error_text = "É necessário informar um nome."
            mensagem_nome_inserido.value = ""
            mensagem_lista_vazia.value = ""
        else:
            nome.error_text = ""
            lista_nomes.append(nome.value) #adiciona o nome na lista
            mensagem_nome_inserido.value = f"O nome '{nome.value}' foi gravado com sucesso!"
            mensagem_lista_vazia.value = ""
            nome.value = "" #limpa o campo de texto
        page.update()
        
    def exibir_nomes(e):
        if not lista_nomes:
            mensagem_lista_vazia.value = "Nenhum nome cadastrado."
            mensagem_nome_inserido.value = ""
        else:
            mensagem_lista_vazia.value = ""
            mensagem_nome_inserido.value = ""
            page.add(ft.Text("Lista de nomes:", size=20, weight="bold", color=ft.Colors.BLACK))
            for i, nome in enumerate(lista_nomes, start=1):
                page.add(ft.Text(f"{i} - {nome}", size=15, weight="bold", color=ft.Colors.BLACK))
        page.update()
        
    def sortear_nome(e):
        if not lista_nomes:
            mensagem_lista_vazia.value = "Nenhum nome cadastrado para sortear."
            mensagem_nome_inserido.value = ""
        else:
            mensagem_lista_vazia.value = ""
            mensagem_nome_inserido.value = ""
            page.add(ft.Text("Nome sorteado: ", size=22, weight="bold", color=ft.Colors.BLACK))
            page.add(ft.Text(random.choice(lista_nomes), size=22, weight="bold", color=ft.Colors.GREEN))
        page.update()

    #declaracao da lista de nomes
    lista_nomes = []
    
    #declaracao de variaveis
    nome = ft.TextField(label="Informe um nome: ")
    botao_gravar_nome = ft.ElevatedButton("Inserir nome", on_click=inserir_nome) 
    botao_exibir_nomes = ft.ElevatedButton("Exibir nomes", on_click=exibir_nomes)
    botao_sortear_nome = ft.ElevatedButton("Sortear nome", on_click=sortear_nome)
    mensagem_nome_inserido = ft.Text(size=20, weight="bold", color=ft.Colors.BLACK)
    mensagem_lista_vazia = ft.Text(size=20, weight="bold", color=ft.Colors.RED)
    
    page.add(
        ft.SafeArea(
            ft.Row(
                [ft.Text(
                        "\nSorteio de Nomes - O sistema escolherá um nome aleatório!", 
                        style=ft.TextThemeStyle.TITLE_LARGE,
                        weight="bold",
                        size=30                        
                        )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ),
        nome,
        ft.Row(
            [
                botao_gravar_nome,
                ft.Text("  "),
                botao_exibir_nomes,
                ft.Text("  "),
                botao_sortear_nome
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        mensagem_nome_inserido,
        mensagem_lista_vazia
    )


ft.app(main)
