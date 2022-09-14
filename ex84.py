'''faça um programa que leia o nome e peso de várias
pessoas e coloque dentro de uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas(acima de 100).
C) Uma listagem com as pessoas mais leves(abaixo de 75).'''

pessoas = list()
dados = list()
acima = total = 0
abaixo = 9999
maiorpeso = list()
menorpeso = list()

while True:
    dados.append(str(input('Nome: ')).upper())
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N]')).upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida, tente novamente.')
        opcao = str(input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
for c in pessoas:
    if c[1] > acima:
        acima = c[1]
    if c[1] < abaixo:
        abaixo = c[1]
for c in pessoas:
    if acima == c[1]:
        maiorpeso.append(c[0])
    if abaixo == c[1]:
        menorpeso.append(c[0])
print(f'O maior peso foi de {acima:.2f} Kg. Peso de {maiorpeso}.')
print(f'O menor peso foi de {abaixo:.2f} Kg. Peso de {menorpeso}.')

