import pyautogui as p
from datetime import datetime

def limpar_credenciais():
    p.write('git config --global --unset user.name')  # Remove o nome do usuário
    p.press('enter')  # Pressiona enter
    p.write('git config --global --unset user.email')  # Remove o email do usuário
    p.press('enter')  # Pressiona enter

if __name__ == "__main__":

    p.PAUSE = 0.5  

    # msg_commit = input('Digite a mensagem do commit: ')  # Solicita a mensagem do commit'
    data_hoje = datetime.now().strftime('%Y%m%d')     

    limpar_credenciais()  # Chama a função para limpar as credenciais

    p.write('git config --global user.name "CalebeCampos"')  # Adiciona o nome do usuário
    p.press('enter')  # Pressiona enter
    p.write('git config --global user.email "calebe_josue@hotmail.com"')  # Adiciona o email do usuário
    p.press('enter')  # Pressiona enter
    p.write('git status')  
    p.press('enter')  # Pressiona enter
    p.write('git add .')  
    p.press('enter')  # Pressiona entergit config --global --unset user.name
    p.write('git status')  
    p.press('enter')  # Pressiona enter 

    # p.write(f'git commit -m "{msg_commit}"')  # Adiciona a mensagem do commit
    p.write(f'git commit -m "arquivos criados até o dia {data_hoje}"')

    p.press('enter')  # Pressiona enter
    p.write('git push')  # Adiciona o push
    p.press('enter')  # Pressiona enter

    limpar_credenciais()  # Chama a função para limpar as credenciais
