mochila = ('machado', 'camisa', 'bacon')
print(mochila)

print('===========')
print(mochila[0])
print(mochila[1])
print(mochila[2])
print(mochila[0:2])
print(mochila[-1])

print('===========')

for item in mochila:
    print('na minha mochila tem: {}' .format(item))

print('======DESEMPACOTAMENTE DE TUPLAS=====')

def soma(*num):
    soma = 0
    print('tupla: {}' .format(num))
    for i in num:
        soma += i
    return soma

#programa principal
print('resultado: {}\n' .format(soma(1,2)))
print('resultado: {}\n' .format(soma(1,2,3,4,5,6,7,8,9)))