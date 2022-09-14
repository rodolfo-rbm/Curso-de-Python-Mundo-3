palavras = ('Sao Paulo', 'Corinthians', 'Santos', 'Palmeiras',
            'Internacional', 'Gremio', 'Juventude', 'Joinville',
            'Fortaleza', 'Coritiba', 'Flamengo', 'Vasco', 'Fluminense')

cont = 0

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end='')