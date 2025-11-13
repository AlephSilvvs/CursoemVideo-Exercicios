"""Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR."""

# Dicionario de cores
cor = {'limpa':'\033[m',
       'azul':'\033[1;34m',
       'vermelho':'\033[1;31m',}

# Pergunta ao usuário
numero = int(input(f'{cor['azul']}Me diga um número qualquer: {cor['limpa']}'))

# Divide por 2, a " % " indica o resto da divisão
resultado = numero % 2

# Se o resto da divisão for igual á, então...
if resultado == 0:
    print(f'O número {numero} é {cor['vermelho']}PAR{cor['limpa']}')
else:
    print(f'O número {numero} é {cor['vermelho']}IMPAR{cor['limpa']} ')
