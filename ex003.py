'''Crie um programa que leia dois números e mostre as soma entre eles.'''

#pegunta o numero
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numro: '))

#soma os numeros
resultado = n1 + n2

#mostra na tela o resultado com cor vermelha
print (f'\033[31mA soma entre {n1} e {n2} é igual a {resultado}\033[m')