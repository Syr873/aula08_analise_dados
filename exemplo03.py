# ---------Funcoes--------------------> Funçoes sempre acima antes do programa!

def saudacao(n, i):
    print(f'Olá {n}, sua idade é {i} anos.')


def soma(n1, n2):
    total = n1 + n2
    print(f'A soma de {n1} e {n2} é: \n{total}')


def  maior_numero(num1, num2):
     if num1 > num2:
         print(f'Maior: {num1}!')
     elif num2 > num1:
         print(f'Maior: {num2}')
     else:
         print('Iguais!')


def soma_pares(x, y):
    total = x + y
    print(f' A soma do par é: {total}')
    lista_pares.append(total)
    print(f'Lista de pares: {lista_pares}')

lista_pares = []
# ----------Programas------------------> Programas sempre abaixo das Funçoes!
         
# ----------------------------------> Saudacao
# nome = input('Informe o nome: ')
# idade = input('Informe a idade: ')
# saudacao(nome, idade)

# ----------------------------------> Soma
# valor01 = int(input('Informe o primeiro valor: '))
# valor02 = int(input('Informe o segundo valor: '))
# soma(valor01, valor02)


# ----------------------------------> Descobre o maior
# numero01 = float(input('Informe o primeiro numero: '))
# numero02 = float(input('Informe o segundo numero: '))
# maior_numero(numero01, numero02)


# ----------------------------------> Soma de três pares
for n in range(3):
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    soma_pares(n1, n2)
 




# ----------------------------------------




