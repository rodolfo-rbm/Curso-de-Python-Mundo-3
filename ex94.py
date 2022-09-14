'''Crie um programa que leia nome, sexo e idade de várias
pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
import copy

pessoa = dict()
dados = []
idadesoma = 0
mulheres = []
maioridade = dict()
while True:
    pessoa['nome'] = str(input('Digite seu nome: ')).title()
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        print('ERRO! Por favor, digite uma opção válida.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    idadesoma += pessoa['idade']
    dados.append(pessoa.copy())
    if pessoa['idade'] >= 40:
        maioridade = pessoa.copy()
    pessoa.clear()
    opcao = str(input('Deseja continuar? [S/N] ')).upper()
    while opcao != 'S' and opcao != 'N':
        print('ERRO! Por favor, digite uma opcão válida.')
        opcao = str(input('Deseja continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print(f'Ao todo temos {len(dados)} pessoas cadastradas.')
media = idadesoma/len(dados)
print(f'A média de idade é de {media:.2f} anos.')
print('As mulheres cadastradas foram ', end=' ')
for c in mulheres:
    print(f'{c} ', end=' ')
print()
print('lista de pessoas cadastradas que estão acima da média:')
for c in dados:
    if c['idade'] >= media:
        print('   ')
        for k, v in c.items():
            print(f'{k} = {v}', end='; ')


