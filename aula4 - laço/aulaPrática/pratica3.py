valor = int(input('Digite o valor em R$ '))
while True:
    if (valor >= 100):
        cont100 = valor // 100
        valor -= cont100 * 100
        print('Cedulas de 100: {}' .format(cont100))
        if not valor:
            break

    if (valor >= 50):
        cont50 = valor // 50
        valor -= cont50 * 50
        print('Cedulas de 50: {}' .format(cont50))
        if not valor:
            break

    if (valor >= 20):
        cont20 = valor // 20
        valor -= cont20 * 20
        print('Cedulas de 20: {}' .format(cont20))
        if not valor:
            break

    if (valor >= 10):
        cont10 = valor // 10
        valor -= cont10 * 10
        print('Cedulas de 10: {}' .format(cont10))
        if not valor:
            break

    if (valor >= 5):
        cont5 = valor // 5
        valor -= cont5 * 5
        print('Cedulas de 5: {}' .format(cont5))
        if not valor:
            break

    if valor:
        cont1 = valor
        print('Cedulas de 1: {}' .format(cont1))
        break