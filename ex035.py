"""Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não
formar um triâgulo."""


print ('-='*20)
print ('Analisador de Triângulos')
print ('-='*20)

# Pegunta ao usuário
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Condição se...
if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulos!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
