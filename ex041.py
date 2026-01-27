"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infatil
-Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master"""

# Biblioteca para pegar data do computador
from datetime import date
ano_atual = date.today().year

# Pergunta o ano
ano_nasci = int(input('Que anos você nasceu? '))

# Operação para transformar ano em idade
idade = ano_atual - ano_nasci

# Condição
if idade <= 9:
    print(f'MIRIM')

elif idade <= 14:
    print('Infantil')

elif idade <= 19:
    print('Junior')

elif idade <= 20:
    print('Sênior')

else:
    print(f'MASTER')