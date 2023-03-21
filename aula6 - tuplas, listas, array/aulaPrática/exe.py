palavras = ('luis', 'maria', 'sabrina', 'mario', 'pedro')

for palavra in palavras:
    print('\n palavra: {}. Vogais: ' .format(palavra.upper()), end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')