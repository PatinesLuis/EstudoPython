x = 1

while (x <=5):
    print(x)
    x = x + 1

    #imprima na tela somente os valores dentro de um intervalo especificado pelo usuário e que seja números pares
inicial = int(input('qual valor deseja iniciar a contagem'))
final = int(input('qual valor deseja encerrar a contagem'))

x = inicial
while(x <= final):
    if(x % 2 == 0):
        print(x)
    x = x + 1