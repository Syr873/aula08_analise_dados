def valor_total(x, y):
    total = x * y
    return total
   

for n in range(3):
    print(f'Venda {n+1}: \n')
    preco = float(input('Informe o preço do produto: '))
    qtd = int(input('\nInforme a quantidade do produto: '))
    preco_final = valor_total(preco, qtd)
    print(f'Preço: {preco:.2f} \nQuantidade: {qtd} \nPreço total: {preco_final:.2f}\n')