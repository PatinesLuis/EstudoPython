print('BEM VINDO A LOJA DO LUIS EDUARDO PATINES!')

valor = float(input('Digite o valor do produto: '))
qtd = int(input('Digite a quantidade: '))

semFrete = valor * qtd #calculo do valor vezes a quantidade

print(f'O valor sem frete foi de: {round(semFrete, 2)} R$') #arredondamento de duas casas decimais,


if qtd > 0 and qtd <= 10: #verificando se a quantidade está entre 0 a 10 
    frete = 30.00
    comFrete = semFrete + frete # soma do valor sem frente com o valor do frete
    print(f'O valor com frete foi de: {round(comFrete, 2)} R$    (frete de R$ {frete})')

elif qtd >= 11 and qtd <= 100: #verificando se a quantidade está entre 11 a 100
    frete = 60.00
    comFrete = semFrete + frete 
    print(f'O valor com frete foi de: {round(comFrete, 2)} R$    (frete de R$ {frete})')

elif qtd >= 101 and qtd <= 1000: #verificando se o quantidade está entre 101 a 1000
    frete = 120.00
    comFrete = semFrete + frete 
    print(f'O valor com frete foi de: {round(comFrete, 2)} R$    (frete de R$ {frete})')

elif qtd >= 1001: #verificando se o quantidade é maior que 1000
    frete = 240.00
    comFrete = semFrete + frete 
    print(f'O valor com frete foi de: {round(comFrete, 2)} R$    (frete de R$ {frete})')

else:
    print('Sem quantidade! programando encerrando') #validando, pois não tem como comprar um produto sem uma quantidade