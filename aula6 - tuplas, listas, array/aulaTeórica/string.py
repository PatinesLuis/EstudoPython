mochila = ['machado','camisa','bacon','abacate']
print(mochila[0][0])
print(mochila[3][3])

for item in mochila:
    for letra in item:
        print(letra, end='-')
    print()