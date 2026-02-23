"""Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

- Abaixo de 18.5: Abaixo do peso
- entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida"""

# Variáveis
altura = float(input('Qual a sua altura? (Kg) '))  # Pergunta ao usuário
peso = float(input('Qual o seu peso? (m) '))
imc =  peso / (altura ** 2)                          # Calculo do IMC

print(f'O IMC dessa pessoa é de {imc:.1f}')

# Estrutura condicional aninhada para cada classificação
if 18.5 > imc:
    print('Você está ABAIXO DO PESO normal')

elif 18.5 <= imc < 25:
    print('PARABÉNS,você está na faixa de PESO NORMAL')

elif 25 <= imc <30:
    print('Você está em SOBREPESO')

elif 30 <= imc < 40:
    print('Você está em OBESIDADE!!')

else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!!!')
