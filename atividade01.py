vendedores = []

for n in range(3):
    print(30 * '=')
    print(f'Vendedor {n + 1}: \n')
    nome = input('Informe o nome do vendedor: ')

    vendas = []
    for i in range(5):
        venda = int(input(f'Informe a quantidade da venda {i + 1}: '))

        vendas.append(venda)
        soma = sum(vendas)
    media = soma / len(vendas)

    vendedor = {
        'Vendedor': nome,
        'Vendas': vendas,
        'Total': soma,
        'Media': round(media,2)
    }

    vendedores.append(vendedor)

for v in vendedores:
    print(30 * '--')
    print(f"Vendedor: {v['Vendedor']}\n")
    print(f"Lista de vendas: {v['Vendas']}\n")
    print(f"Total de vendas: {v['Total']}\n")
    print(f"Media de vendas: {v['Media']}\n")
    
     
