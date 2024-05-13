soma=0
c = 0
alunos = int(input("Digite a quantidade de alunos: "))
while c < alunos:
    Notas = float(input("Digite a nota aqui:"))
    soma = soma + Notas
    c = c + 1
media = soma /alunos
print(f" A média da sala é {media}")
