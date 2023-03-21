print('Bem vindo a sorveteria do Luis Eduardo Patines')

print('------------------------------Cardápio--------------------------')
print('| Código | Descrição            | Tamanho P(500ml) | Tamanho M(1000ml) | Tamanho G(1000ml)|')
print('|   TR   | sabores tradicionais |     R$ 6,00      |    R$ 10,00       |      R$ 18,00    |')
print('|   ES   | sabores especiais    |     R$ 7,00      |    R$ 12,00       |      R$ 21,00    |')
print('|   PR   | sabores premium      |     R$ 8,00      |    R$ 14,00       |      R$ 24,00    |')

dinheiro = 0

soma = 0

while True:
    tamanho = input('Entre com o TAMANHO do pote desejado (P/M/G): ').upper()
    if(tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print('TAMANHO INVALIDO!')
        continue #caso o cliente digite um tamanho diferente, irá pedir para digitar novamente

    codigo = input('Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ').upper()
    if(codigo != 'TR' and codigo != 'ES' and codigo != 'PR'):
        print('CÓDIGO INVALIDO!')

        continue #caso o cliente digite um código diferente, irá pedir para digitar novamente

    if codigo == 'TR' and tamanho == 'P': # validação de pedidos da descrição 'sabores tradicionais'
            soma = 6
            print('Você pediu um sorvete sabor tradicional P de R$ 6,00')
            dinheiro += soma      

    elif codigo == 'TR' and tamanho == 'M':
            soma = 10
            print('Você pediu um sorvete sabor tradicional M de R$ 10,00')
            dinheiro += soma 

    elif codigo == 'TR' and tamanho == 'G':
            soma = 18
            print('Você pediu um sorvete sabor tradicional P de R$ 18,00')
            dinheiro += soma 

    elif codigo == 'ES' and tamanho == 'P': # validação de pedidos da descrição 'sabores especiais'
            soma = 7
            print('Você pediu um sorvete sabor ESPECIAL P de R$ 7,00')
            dinheiro += soma 

    elif codigo == 'ES' and tamanho == 'M':
            soma = 12
            print('Você pediu um sorvete sabor ESPECIAL M de R$ 12,00')
            dinheiro += soma

    elif codigo == 'ES' and tamanho == 'G':
            soma = 21
            print('Você pediu um sorvete sabor ESPECIAL G de R$ 21,00')
            dinheiro += soma 

    elif codigo == 'PR' and tamanho == 'P': # validação de pedidos da descrição 'sabores premium'
            soma = 8
            print('Você pediu um sorvete sabor PREMIUM P de R$ 8,00')
            dinheiro += soma     

    elif codigo == 'PR' and tamanho == 'M':
            soma = 14
            print('Você pediu um sorvete sabor PREMIUM M de R$ 14,00')
            dinheiro += soma 

    elif codigo == 'PR' and tamanho == 'G':
            soma = 24
            print('Você pediu um sorvete sabor PREMIUM G de R$ 24,00')
            dinheiro += soma     
    print('==========================================================')

    op = input('Deseja pedir mais alguma coisa? (S/N): ')
    if op != 'N': #opção caso o cliente queira encerrar o pedido
        continue
    else:
        break
print('O total a ser pago é: R${},00' .format(dinheiro))