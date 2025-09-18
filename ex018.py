"""Faça um programa que leia uma âgulo qualque e mostre na tela o valor do seno, cosseno e tangente
desse ângulo"""

# Dicionario de cores
cor = {'limpa':'\033[m',
       'azul':'\033[1;34m',
       'vermelho':'\033[1;31m',
       'verde':'\033[32m','branco':'\033[1;38m'}

# Importa a biblioteca
from math import radians, sin, cos, tan

# Pergunta o ângulo
angulo = float(input(f'{cor['branco']}Digite o âgulo que você deseja:{cor['limpa']} '))

# Calcula o Seno, Cosseno, Tangente e printa
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print(f'\nO ângulo de {angulo} tem o {cor['azul']}SENO de {seno:.2f}{cor['limpa']}')
print(f'O âgnulo de {angulo} tem o {cor['verde']}COSSENO de {cosseno:.2f}{cor['limpa']}')
print(f'O ângulo de {angulo} tem a {cor['vermelho']}TANGENTE de {tangente:.2f}{cor['limpa']}')