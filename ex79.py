'''crie um programa onde o usuário possa digitar vários valores
númericos e cadastre-os em uma lista. Caso o número já exista
 la dentro, ele não será adicionado. No final, serão exibidos
 todos os valores únicos digitados, em ordem crescente.'''

numeros = list()

while True:
    n = (int(input('Digite um valor: ')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado...Não será adicionado a lista.')
    opcao = str(input('Deseja continuar? [S/N]')).upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida, tente novamente...')
        opcao = str(input('Deseja continuar? [S/N]')).upper()

    if opcao == 'N':
        break
numeros.sort()
print(f'-='*20)
print(f'Você digitou os valores', *numeros, sep=' ')
print(f'-='*20)
