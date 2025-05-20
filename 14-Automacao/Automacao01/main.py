import pyautogui as auto # necessario fazer o pip install pyautogui visto que o pyautogui não é nativo do python

auto.PAUSE = 0.5 # tempo de espera entre os comandos

# funcao press executa a acao de pressionar uma tecla do teclado
auto.press('win') # abre o menu iniciar

# funcao write escreve o texto desejado
auto.write('firefox') # escreve firefox no menu iniciar
auto.press('enter') # pressiona enter para abrir o firefox

# funcao hotkey executa a acao de pressionar uma combinacao de teclas do teclado
auto.hotkey('alt', 'space') 
auto.press('x') # maximiza a tela do firefox
auto.write('python') # escreve python na barra de endereços
auto.press('enter') # pressiona enter para abrir o python
auto.hotkey('ctrl', 't') # abre uma nova aba no firefox
auto.write('sistemafibra.org.br') # escreve o link do google na barra de endereços
auto.press('enter') # pressiona enter 