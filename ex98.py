"""Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo. O seu programa
tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
from time import sleep


def contador(a, b, c):
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print('-=' * 30)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont <= b:
            print(cont, end=' ')
            cont += c
            sleep(0.5)
        print('FIM')
    else:
        cont = a
        while cont >= b:
            print(cont, end=' ')
            cont -= c
            sleep(0.5)
        print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
