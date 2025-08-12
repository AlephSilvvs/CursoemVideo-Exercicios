"""Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada."""

# Dicionario de cores
cor = {'limpa':'\033[m',
       'azul':'\033[34m',
       'vermelho':'\033[31m',
       'verde':'\033[32m',
       'branco':'\033[1;38m'}

#pergunta o numero
num = int(input(f'{cor['branco']}Digite um número:{cor['limpa']} '))

# Mostra o resultado com operações e cores
print(f'{cor['azul']}O dobro de {num} vale {num*2}. {cor['limpa']}')

print(f'{cor['verde']}O triplo de {num} vale {num*3}.{cor['limpa']} '
      f'\n{cor['vermelho']}A raiz quadrada de {num} é igual a {num**(1/2):.2f}.{cor['limpa']}')