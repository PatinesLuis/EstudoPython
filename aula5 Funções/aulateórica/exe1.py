def borda(s1):
    tam = len(s1)

    if(tam):
        print('+','-' * tam, '+')
        print('|', s1, '|')
        print('+','-' * tam, '+')

    else:
        print("Não digitou nada")


while True:
    dig = input('Digite uma palavra: ')
    

    if dig != '':
        break
    print('Você não digitou nada! Digite algo: ')

borda('Hello word!')
borda(dig)