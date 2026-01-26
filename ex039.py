"""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

# Biblioteca, pega o ano atual do computador
from datetime import date
ano_atual = date.today().year

# Pergunta o ano de nascimento
ano = int(input('Que ano você nasceu? '))

# Faz o calculo da idade
idade = ano_atual - ano

# Condição
if idade == 18:
    print(f'Você tem {idade} anos, está na hora de se alistar')
elif idade < 18:
    print(f'Ainda não chegou a hora de se alistar, falta {18-idade} anos')
else:
    print(f'Já passou da hora de se alistar, passaram {idade-18} anos')

