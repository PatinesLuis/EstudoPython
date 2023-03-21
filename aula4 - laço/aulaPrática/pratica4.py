total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade?')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    
    if(idade < 3):
        dinheiro = 0

    else:
        if(idade >12):
            dinheiro = 30
    
        else:
            dinheiro = 15
    
    dinheiro += dinheiro

print('Total de pessoas: {}' .format(total))
print('total arrecado: {}' .format(dinheiro))
