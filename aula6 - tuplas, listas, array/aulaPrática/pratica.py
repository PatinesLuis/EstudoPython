lista = [9,8,7,7,3,4,5,7]

print(lista.count(7))

print('ENCONTRAR A MAIOR NOTA')
print(max(lista,key=int))

print('ORDENAR')
print(sorted(lista))

print('A MEDIA DAS NOTAS')

qtd = len(lista)
soma = sum(lista)
media = soma/qtd

print('São {} notas. A média é:{}' .format(qtd, media))