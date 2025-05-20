"""
Crie um programa que commit a o projeto em python e envia o repositório local para o remoto
"""

import pyautogui as gui

gui.PAUSE = 0.5 # tempo de espera entre os comandos

gui.press('win')
gui.write('cmd')
gui.press('enter')
gui.write('cd C:\\Users\\ead\\Aperfeicoamento em python (Calebe Campos)')
gui.press('enter')
gui.write('git status')
gui.press('enter')
gui.write('git add .')
gui.press('enter')
gui.write('git status')
gui.press('enter')
# gui.write('git commit -m "commit inicial"')
# gui.press('enter')
# gui.write('git push')
# gui.press('enter')