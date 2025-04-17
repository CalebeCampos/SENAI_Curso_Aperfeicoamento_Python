from deep_translator import GoogleTranslator
#executar no terminal: pip install deep-translator

try:
    
    tradutor = GoogleTranslator(source='auto', target='pt')
    
    while True:

        texto_original = input("Digite o texto a ser traduzido: ")
        texto_traduzido = tradutor.translate(texto_original)

        print(f"Texto traduzido: {texto_traduzido}\n")

        encerrar = input("Deseja traduzir outro texto? (s/n): ")

        match encerrar:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida.")

except Exception as e:
    print(f"Nao foi possivel traduzir. Erro: {e}.")
