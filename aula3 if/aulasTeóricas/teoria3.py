produto = int(input('Qual opção deseja 1- Maça | 2- Laranja | 3- Banana:   '))


if (produto == 1):
    qtd = int(input('Quantas unidades'))
    pagar = qtd * 2.3
    print('Você comprou {} maças. Total a pagar: {};' .format(qtd, pagar))
else:
    if(produto == 2):
        qtd = int(input('Quantas unidades'))
        pagar = qtd * 3.6
        print('Você comprou {} Laranjas. Total a pagar: {};' .format(qtd, pagar))
    else:
        if(produto == 3):
            qtd = int(input('Quantas unidades'))
            pagar == qtd * 1.85
            print('Você comprou {} bananas. Total a pagar: {};' .format(qtd, pagar))
        else:
            print('Produto inexistente')