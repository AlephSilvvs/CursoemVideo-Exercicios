"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""


from random import randint # Randomizar entre uma sequecia
from time import sleep  # Temporizar

# Faz o computador "Pensar"
computador = randint(0,5)

print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

# Jogador tenta acertar
jogador = int(input('Em que numero eu pensei? '))

# Faz esperar
print('PROCESSANDO...')
sleep(3)

# Resultado
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')