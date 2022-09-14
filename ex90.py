'''Faça um programa que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.'''

pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: ')).title()
pessoa['media'] = float(input('Digite sua média: '))
if pessoa['media'] < 5:
    pessoa['situação'] = 'Reprovado'
elif pessoa['media'] >= 5 and pessoa['media'] < 7:
    pessoa['situação'] = 'Recuperação'
elif pessoa['media'] >=7:
    pessoa['situação'] = 'Aprovado'
print('-='*30)
for k, v in pessoa.items():
    print(f'- {k} é igual a {v}')
