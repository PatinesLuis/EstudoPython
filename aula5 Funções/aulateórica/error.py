
while True:
    try: #tentar executar
        x = int(input('Digite um numero'))
        break
    except ValueError:
        print('ooops! Numero invalido, tente novamente')