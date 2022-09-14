'''Crie um programa onde o usuário possa digitar sete
valores númericos e cadastre-os em uma lista única que
mantenha separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.'''

'''lista = []

for c in range(0, 7):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
lista.sort()
print(f'os pares são: ', end='')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
print(f'\nOs ímpares são: ', end='')
for c in lista:
    if c % 2 == 1:
        print(c, end=' ')''' #jeito que eu fiz

lista = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-='*30)
print(f'Os valores pares foram: {lista[0]}')
print(f'Os valores ímpares foram: {lista[1]}')
