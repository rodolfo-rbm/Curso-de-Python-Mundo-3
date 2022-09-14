'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

valores = []

while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar? [S/N]')).upper()
    while opcao != 'S' and opcao != 'N':
        print('Opção inválida, tente novamente...')
        opcao = str(input('Deseja continuar? [S/N]')).upper()

    if opcao == 'N':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescentes são {valores}')
if 5 in valores:
    print(f'Ovalor 5 faz parte da lista')
else:
    print(f'O valor 5 não foi encontrado na lista')
