Nalunos = int(input("Digite a quantidade de alunos: "))
soma=0
for x in range(Nalunos):
    Notas = float(input("Digite a nota aqui:"))
    soma = soma + Notas
media = soma/Nalunos
print(f" A média da sala é {media}")