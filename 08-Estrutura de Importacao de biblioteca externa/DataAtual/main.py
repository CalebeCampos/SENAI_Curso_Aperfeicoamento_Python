#importando apenas a funcao date da bibioteca datetime
#importando apenas o modulo date da biblioteca datetime
from datetime import date

data_atual = date.today() # Atribui a data atual a variavel data_atual

print(f"Data atual: {data_atual}") # Imprime a data atual no formato YYYY-MM-DD

dia = data_atual.day # Atribui o dia atual a variavel dia
mes = data_atual.month # Atribui o mes atual a variavel mes
ano = data_atual.year # Atribui o ano atual a variavel ano

print(f"Data atual: {dia}/{mes}/{ano}") # Imprime a data atual no formato DD-MM-YYYY
