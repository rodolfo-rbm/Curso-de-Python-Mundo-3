"""Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
O seu programa tem que analisar todos os valores e dizer qual
deles é o maior."""
from time import sleep


def maior(*num):
    cont = maior = 0
    print('-'*30)
    print('Analisando os dados passados...')
    for c in num:
        print(f'{c} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor informado foi {maior}.')
    sleep(0.5)


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
