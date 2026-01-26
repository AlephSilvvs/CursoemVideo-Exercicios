"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infatil
-Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master"""

from datetime import date
ano_atual = date.today().year

ano_nasci = int(input('Que anos você nasceu? '))

idade = ano_atual - ano_nasci

if idade <= 9:
    print(f'MIRIM')

else:
    print(f'MASTER')