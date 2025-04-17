import calendar
from datetime import date

mes = date.today().month # Atribui o mes atual a variavel mes
ano = date.today().year # Atribui o ano atual a variavel ano

print(calendar.month(ano, mes)) # Imprime o calendario do mes e ano passados como parametros
