'''Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade
de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''
from time import sleep
jogador = dict()
dados = list()
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: ')).title()
jogador['partida'] = int(input(f'Quantas patidas {jogador["nome"]} jogou? '))
for c in range(0, jogador['partida']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    total += gols[c]
jogador['gols'] = gols[:]
jogador['total'] = total
dados.append(jogador.copy())
print('-='*30)
print(dados)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
    sleep(0.5)
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partida"]} partidas.')
for c in range(0, jogador['partida']):
    print(f'=> Na partida {c+1}, fez {gols[c]} gols.')
    sleep(0.5)


