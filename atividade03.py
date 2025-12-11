def multa(p):
    kg = p - 100
    multa = kg * 4
    return multa

# programa
peso = float(input('Informe quantidade de peixes pescados neste dia(em kg): '))
if peso > 100:
    total = multa(peso)
    print(f'Peso max. 100 kg excedido! \nMulta de R$4.00 por kg: R${total:.2f}')
else:
    print('Peso max. 100 kg não excedido! Sem multas...')