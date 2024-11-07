# solicita os 5 números aos usúarios
alunos = []
notas = []

for i in range (5):
    aluno = input ("digite o nome do aluno: ")
    nota =  int(input("digite a nota do aluno:"))
    alunos.append(aluno)
    notas.append(nota)

for i in range (5):
    print(f"o aluno {alunos[i]}tirou nota{notas[i]}")