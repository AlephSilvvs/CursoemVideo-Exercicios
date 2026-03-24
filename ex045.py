"""Crie um programa que faça o computador jogar jokenpô com você."""

# Bibliotecas usadas
from random import randint
from time import sleep        # Biblioteca para temporizar

# Lista
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# Pergunta ao usuario
print(f'O computador escolheu  {itens[computador]}')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))

# Temporizando a resposta com Jokenpo
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

# Mostrando qual foi o escolhido do PC x Usuário
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

# Condição aninhada para ver quem venceu
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('ENPATE')
    else:
        print('JOGADA INVÁLIDA!')