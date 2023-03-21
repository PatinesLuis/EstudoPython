mochila = ['machado','camisa','bacon','abacate']
print('lista: ', mochila)

print('==================')

mochila.append('Ovos') #adicionar novo item
print('Lista append:', mochila)

mochila.insert(1,'canivete') #adicionar novo item e escolher a posição dele
print('Lista insert:', mochila)

del mochila[2] #escolher qual posição remover
print('Lista del:', mochila)

mochila.remove('Ovos') #escolher o item para remover
print('Lista remove:', mochila)

print('========COPIAS DE LISTA==========')

x = [5,7,9,11]
y = x[:]

y[0] = 2

print(x)
print(y)