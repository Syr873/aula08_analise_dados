alunos = []

for n in range(5):
    print(f'\n----- Aluno{n + 1}')
    nome = input('Informe o nome do aluno: ')
    
    notas = []
    for i in range(5):
        nota = float(input(f'Informe a nota {i + 1}: '))
        notas.append(nota)
    
    media = sum(notas) / len(notas)

    aluno = {
        'Nome do aluno': nome,
        'Notas': notas,
        'Media': media
    }

    alunos.append(aluno)

# Exibindo os dados
for estudante in alunos:
    print(f"Nome: {estudante['Nome do aluno']}\n")
    print(f"Notas: {estudante['Notas']}\n")
    print(f"Media: {estudante['Media']}\n")



    


