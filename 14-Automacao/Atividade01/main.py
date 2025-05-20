"""
Crie um programa que commit a o projeto em python e envia o repositório local para o remoto
"""

import pyautogui as gui
from datetime import datetime

# Obtém a data de hoje no formato desejado
data_hoje = datetime.now().strftime('%Y/%m/%d')

gui.PAUSE = 0.5 # tempo de espera entre os comandos

gui.press('win')
gui.write('cmd')
gui.press('enter')
gui.write('cd C:\\Users\\ead\\Aperfeicoamento em python (Calebe Campos)')
gui.press('enter')
gui.write('git config --global --unset user.name')
gui.press('enter')
gui.write('git config --global --unset user.email')
gui.press('enter')
gui.write('git config --global user.name "Calebe Campos"')
gui.press('enter')
gui.write('git config --global user.email "calebe_josue@hotmail.com"')
gui.press('enter')
gui.write('git status')
gui.press('enter')
gui.write('git add .')
gui.press('enter')
gui.write('git status')
gui.press('enter')
gui.write(f'git commit -m "arquivos criados até o dia {data_hoje}"')
gui.press('enter')
gui.write('git push')
gui.press('enter')