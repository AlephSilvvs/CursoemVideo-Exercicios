"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infatil
-Até 19 anos: Junior
- Até 25 anos: Sênior
- Acima: Master"""

# Biblioteca para pegar data do computador
from datetime import date

# Variáveis
ano_atual = date.today().year                       # Ano atual do computador
ano_nasci = int(input('Ano de Nascimento: '))    # Pergunta ao usuário
idade = ano_atual - ano_nasci                       # Transformar ano em idade

print(f'O atleta tem {idade} anos.')

# Condição Aninhada para a classificação
if idade <= 9:
    print(f'Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print(f'Classifficação: MASTER')
