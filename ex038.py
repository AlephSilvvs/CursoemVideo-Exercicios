"""Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é Maior
- O segundo valor é Maior
- Não existe valor maior, os dois são iguais"""

# Pedindo um número
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))

# Condição, testando qual valor é maior
if num1 > num2:
    print(f'O primeiro valor é maior')
elif num2 > num1:
    print(f'O segundo valor é maior')
else:
    print(f'Não existe valor maior, os dois são iguais')