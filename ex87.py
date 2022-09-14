'''aprimore o desafio anterior, mostrando no final:
A) a soma de todos os valores pares.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha = []
par = 0
soma = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = (int(input(f'Valor para [{l, c}]: ')))
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

for l in range(0, 3):
    soma += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma de todos os valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
