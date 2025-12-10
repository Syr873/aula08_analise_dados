# Funcoes --> Funçoes sempre acima antes do programa!

def saudacao(n, i):
    print(f'Olá {n}, sua idade é {i} anos.')



def soma(n1, n2):
    total = n1 + n2
    print(f'A soma de {n1} e {n2} é: \n{total}')

# Programas --> Programas sempre abaixo das Funçoes!
    
# nome = input('Informe o nome: ')
# idade = input('Informe a idade: ')
# saudacao(nome, idade)


valor01 = int(input('Informe o primeiro valor: '))
valor02 = int(input('Informe o segundo valor: '))
soma(valor01, valor02)