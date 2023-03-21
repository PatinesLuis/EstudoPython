import random

def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while((x < min) or (x > max)):
        x = int(input(pergunta)) 
    return x

def vencedor(j1,j2):
    global empate, v1, v2
    if j1 ==1: # pedra
        if j2 ==1: # pedra
            embate += 1

        elif j2 ==2: #papel
            v2 += 1

        elif j2 ==3: #tesoura
            v1 += 1
    
    elif j1 ==2: #papel
        if j2 ==1: # pedra
            v1 +=1

        elif j2 ==2: #papel
            empate += 1

        elif j2 ==3: #tesoura
            v2 +=1


    elif j1 ==3: #tesoura
        if j2 ==1: # pedra
            v2 +=1

        elif j2 ==2: #papel
            v1 +=1
            

        elif j2 ==3: #tesoura
            empate +=1

    resultados = [v1,v2,empate]
    return resultados

#programa principal
print('JOKENPO')
print('1- Pedra')
print('2- Papel')
print('3- Tesoura')

resultados = []
jogadas = []

v1 = 0
v2 = 0
empate = 0

while True:
    j1 = valida_int('\nEscolha sua jogada: ',0,3)
    if j1 == 0:
        break
    j2 = random.randint(1,3)
    jogadas.append(['jogador: ',j1,' bot: ',j2, '\n'])
    resultados = vencedor(j1,j2)


    for jogada in jogadas:
        for dado in jogada:
            print(dado, end='')

print('numero de vitorias do jogador: {}' .format(resultados[0]))
print('numero de vitorias do bot: {}' .format(resultados[1]))
print('numero de empates: {}' .format(resultados[2]))