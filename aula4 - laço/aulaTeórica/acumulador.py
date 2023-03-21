#escreva um algoritmo que calcule a sua média de notas
#vamos assumir que a média é dada por 5 notas digitadas

cont = 1

soma = 0

while(cont <= 5):
    nota = float(input("Digite a nota {}: " .format(cont)))
    soma += nota
    cont += 1

media = soma / cont
print('Media final: {}' .format(media))