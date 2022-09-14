'''crie um programa que tenha uma tupla totalmente
preenchida com uma contagem por extensão, de zero até vinte.
Seu programa deverá ler um número pelo teclado
(entre 0 e 20) e mostra-lo por extenso.'''
entrada = 0
numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
          'dezessete', 'dezoito', 'dezenove', 'vinte')

entrada = int(input('Digite um número de zero a 20: '))
while entrada > 20 or entrada < 0:
    entrada = int(input('Digite um número de zero a 20: '))

print(f'Você digitou o número {numero[entrada]}')





