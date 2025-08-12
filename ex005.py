"""Faça um programa que leia uma número inteiro e mostre na tela o seu sucessor e seu antecessor."""

# Pergunta o numero.
n = int(input('Digite um número: '))

# Mostra na tela o resultado.
print(f'\033[31mAnalisando o valor {n}, seu antecessor é {n-1} e o seu sucessor é {n+2}\033[m') # Operações feitas dentro do format
