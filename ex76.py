'''crie um programa que tenha uma tupla única com nomes de
produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os
de forma tabular.'''

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'mochila', 120.35,
            'livro', 36.89)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for cont in range(0, len(listagem)):
    if cont % 2 == 0:
        print(f'{listagem[cont]:.<30}',end='')
    else:
        print(f'R$ {listagem[cont]:>2.2f}')

