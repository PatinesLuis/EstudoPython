print('Qual produto deseja escolher?')
produto = int(input('1- MAÇA | 2- LARANJA | 3-BANANA'))

if(produto == 1):
    qtd = int(input('Quantas maças deseja pegar: '))
    pagar = qtd * 2.30
    print('Você comprou {} maças. Total a pagar: {};' .format(qtd, pagar))

elif(produto == 2):
    qtd = int(input('Quantas laranjas deseja pegar: '))
    pagar = qtd * 2.36
    print('Você comprou {} Laranjas. Total a pagar: {};' .format(qtd, pagar))

elif(produto == 3):
    qtd = int(input('Quantas Bananas deseja pegar: '))
    pagar = qtd * 1.85
    print('Você comprou {} Bananas. Total a pagar: {};' .format(qtd, pagar))   
else:
    print('Produto inexistente') 
