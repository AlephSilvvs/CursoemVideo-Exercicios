"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome."""

nome = str(input('Digite seu nome completo: ')).strip()  # Colocar o str no codigo, da a possibilidade de uma usar o strip

print(f'Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {(len(nome.replace(' ', '')))} letras')
print(f'Seu primeiro nome tem {nome.find(' ')}')