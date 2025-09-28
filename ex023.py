"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados."""

# Dicionario de cores
cor = {'limpa':'\033[m',
       'azul':'\033[1;34m',
       'vermelho':'\033[31m',
       'verde':'\033[1;32m',
       'marinho':'\033[1;36m',
       'text':'\033[1;33m'}

# Pede um numero
num = int(input('Informe um número: '))

# Faz o calculo
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Mostra na tela
print(f'\nAnalisando o número {cor['vermelho']}{num}{cor['limpa']}')
print(f'{cor['verde']}Unidade: {u}{cor['limpa']}')
print(f'{cor['azul']}Dezena:  {d}{cor['limpa']}')
print(f'{cor['marinho']}Centena: {c}{cor['limpa']}')
print(f'{cor['text']}Milhar:  {m}{cor['limpa']}')