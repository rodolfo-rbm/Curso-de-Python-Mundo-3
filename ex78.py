'''crie um programa que leia 5 valores númericos e guarde numa lista.
No final mostre qual o maior valor e o menor valor e suas respectivas
posições na lista.'''

valor = []
maior = [0]

for c in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))

print('-='*20)
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} na(s) posição(ões) ', end='')
for c, v in enumerate(valor):
    if v == max(valor):
        print(f'{c}...', end='')
print(f'\nO menor valor digitado foi {min(valor)} na(s) posição(ões) ', end='')
for c, v in enumerate(valor):
    if v == min(valor):
        print(f'{c}...', end='')
