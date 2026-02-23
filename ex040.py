"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado"""

nota1 = float(input('Digite sua nota escolar: '))
nota2 = float(input('Digite mais uma nota escolar: '))

media = (nota1 + nota2) / 2

if media < 5:
    print(f'Reprovado')
elif 7 > media <= 5:
    print(f'Recuperação')
else:                   # media >= 7:
    print('Parabens!! Você foi Aprovado')

print(f'{media:.1f}')