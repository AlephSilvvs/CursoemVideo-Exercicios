"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

# Pergunta ao usuário
altura = float(input('Qual a sua altura? '))
peso = float(input('Qual o seu peso? '))

# Calculo do IMC
imc =  peso / altura ** 2

# Estrutura condicional aninhada para cada classificação
if 18.5 > imc:
    print('Abaixo do Peso')
elif 18.5 <= imc <25:
    print('Peso Ideal')
elif 25 <= imc <30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')


print(f'{imc:.2f}')