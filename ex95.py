'''Aprimore o desafio 93 para que ele funcione com vários
jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''

from time import sleep
jogador = dict()
dados = list()
gols = []
total = 0
while True:
    jogador.clear()
    gols.clear()
    total = 0
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    jogador['partida'] = int(input(f'Quantas patidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partida']):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
        total += gols[c]
    jogador['gols'] = gols[:]
    jogador['total'] = total
    dados.append(jogador.copy())
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida...Tente novamente!')
        opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print('='*30)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('='*30)
for c in dados:
    print(f'{dados.index(c):>3} ', end='')
    for k, v in c.items():
        print(f'{str(v):<15}', end='')
    print()
print('='*30)
while True:
    exibir = int(input('Mostrar dados de qual jogador? (999 p/ PARAR) '))
    if exibir != 999:
        break
    if exibir >= len(dados):
        print('Dados inválidos')
    for c in dados:
        if exibir == dados.index(c):
            print(f'Levantamento do jogador {c["nome"]}...')
            for i in range(0, c['partida']):
                print(f'no jogo {i+1} fez {c["gols"][i]} gols.')
