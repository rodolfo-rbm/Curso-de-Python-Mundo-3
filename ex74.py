'''crie um programa que vai gerar 5 numeros aleatorios e
colocar dentro de uma tupla. Depois disso, mostre a listagem
de numeros gerados e tambem indique o menor e o maior valor
que estão na tupla.'''

from random import randint

cont = maior = 0
menor = 999
lista = ''
a = [0, 0, 0, 0, 0]

for cont in range(0, 5):
    numero = randint(0, 10)
    a[cont] = numero
    if maior < a[cont]:
        maior = a[cont]
    elif a[cont] < menor:
        menor = a[cont]
    cont += 1


lista = a
print(f'Os valores sorteados foram: {lista}')
print(f'O maior número sorteado foi {maior}')
print(f'O menor núemro sorteado foi {menor}')
print(f'{max(lista)}')
print(f'{min(lista)}')


