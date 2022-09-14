""" Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno. """


def area():
    a = l * c
    print(f'A area do terreno é de {a:.2f} m².')


print(f'-'*30)
print(f"{'Controle de terrenos':^30}")
print('-'*30)

l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
area()
