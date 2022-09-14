'''crie uma tupla com os 20 primeiros colocados da
tabela do brasileirão, na ordem de colocação e depois mostre:
A - apenas os 5 primeiros colocados
B - Os ultimos 4 colocados.
C - uma lista em ordem alfabetica.
D - em que posição na tabela esta a chapecoense.'''

tabela = ('Atletico-MG', 'Flamengo', 'Pameiras', 'Fotaleza', 'Corinthians', 'Bragantino',
          'Fluminense', 'America-MG', 'Atletico-GO', 'Santos', 'Ceara',
          'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiaba', 'Juventude',
          'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')

print(f'-='*20)
print(f'Lista de times do Brasileirão: {tabela}')
print(f'-='*20)
print(f'Os 5 primeiros colocados são {tabela[:5]}')
print(f'-='*20)
print(f'Os 4 ultimos colocados são {tabela[16:]}')
print(f'-='*20)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print(f'-='*20)
chape = tabela.index('Chapecoense')
print(f'A chapecoense esta na posição {chape + 1}')



