
preco = float(input('Digite o preço do produto'))
desconto = float(input('Digite o percentual de Desconto do tal produto'))

calcDesconto = preco * (desconto /100)

valorDesconto = preco - calcDesconto

print('O valor do preço é de: {}' .format(valorDesconto))