
while True:
    nome = input('Qual seu nome?: ')
    if(nome != 'Eduardo'):
        continue
    senha   = input('Qual sua senha?: ')
    if(senha == 'patines'):
        break

print('Acesso concedido')