"""Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los
na lista e a segunda função vai mostrar a soma entre
todos os valores pares sorteados pela função anterior."""
from random import randint


def sorteia(lista):
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('Pronto')


def somaPar(lista):
    s = 0
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'A soma dos pares é {s}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

