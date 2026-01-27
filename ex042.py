"""Refaça o desafio 035 dos triângulo, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes"""

# Dicionario de Cores
cor = {'limpa':'\033[m',
       'verde':'\033[1;32m',
       'amarelo':'\033[1;33m',
       'azul':'\033[1;34m',
       'vermelho':'\033[054;31m'}


# Moldura visual
print ('-='*20)
print ('Analisador de Triângulos')
print ('-='*20)


# Pergunta ao usuário
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))


# Estrutura condicional aninhada para formar Triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar Triângulo ', end='')        # "End" foi usado para ligar as duas linhas

    if r1 == r2 == r3:                                       # Triangulo Equilátero
     print(f'{cor['verde']}Equilátero {cor['limpa']}')
    elif r1 != r2 != r3 != r1:                               # Triângulo Escaleno
        print(f'{cor['amarelo']}Escaleno {cor['limpa']}')
    else:                                                    # Triângulo Isósceles
        print(f'{cor['azul']}Isósceles {cor['limpa']}')

else:
    print(f'Os segmentos acima {cor['vermelho']}NÃO PODEM FORMAR triângulo!{cor['limpa']}')

