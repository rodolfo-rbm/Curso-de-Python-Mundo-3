'''Crie um programa que leia nome e duas notas de vários
 alunos e guarde tudo em uma lista composta. No final,
 mostre um boletim contendo a média de cada um e permita
 que o usuário possa mostrar as notas de cada aluno individualmente.'''

lista = list()
dados = list()
opcao = ''
while True:
    dados.append(str(input('Digite o nome do aluno: ')))
    dados.append(float(input('Digite a primeira nota: ')))
    dados.append(float(input('Digite a segunda nota: ')))
    lista.append(dados[:])
    dados.clear()
    opcao = str(input('Quer continuar? [S/N]')).upper()
    while opcao != 'S' and  opcao != 'N':
        print('Opção inválida...Tente novamente.')
        opcao = str(input('Quer continuar? [S/N]')).upper()
    if opcao == 'N':
        break

print('='*30)
print('Nº        Nome        Média')
print('-'*30)
for i, l in enumerate(lista):
    print(f'{i}        {l[0]}       {(l[1]+l[2])/2:.2f}')
print('-'*30)
while True:
    flag = int(input('Mostrar notas de qual aluno? (999 para PARAR) '))
    if flag == 999:
        print('Volte sempre!!!')
        break
    for i, l in enumerate(lista):
        if i == flag:
            print(f'As notas do(a) {l[0]} foram {l[1]:.2f} e {l[2]:.2f}')

