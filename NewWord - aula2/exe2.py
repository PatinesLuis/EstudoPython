kmPerc = float(input("Quantidade de km percorrido: "))
dias = int(input("Quantos dias o carro está alugado?"))

preco = 60 * dias + 0.15 * kmPerc

print('Foi gasto no total: {} R$' .format(preco))