"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa."""

# Importando biblioteca
from math import hypot

# Pergunta ao usuario o comprimento
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adijacente: '))

# Faz o calculo da hipotenusa e mostra na tela
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')