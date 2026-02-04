"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual se será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal"""

# Pede um número
num = int (input('Digite um número inteiro: '))


# Mostra as opções
print ('''Escolha uma das bases para conversão
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL ''')


# Resposta
opção = int(input('Sua opção: '))


# Condição Aninhada
if opção == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num) [2:]} ')  # O [2:] é uma técnica de fatiamento para não mostrar os 2 primeiros, pulando 2 casas, a 0 e a 1
elif opção == 2:
    print(f'{num} convertido para OCTAL {oct(num) [2:]} ')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num) [2:]} ')
else:
    print('Opção inválida. Tente novamente.')