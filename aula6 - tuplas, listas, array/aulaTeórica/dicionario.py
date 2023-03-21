game = {
    'nome':'Super Mario',
    'desenolvedora':'Nintendo',
    'ano':1990
}
print(game)
print(game['nome'])
print(game['ano'])

for i in game.values():
    print(i)
print('==================')
for i in game.keys():
    print(i)

print('==================')

for i,j in game.items():
    print('{} = {}' .format(i,j))



