notas = ["","","","",""]
soma = 0
acima = 0
for x in range(5):
    notas[x] = float(input("Digite a nota do aluno: "))
for y in range(5):
    soma = soma + notas[y]
media = soma/5
for z in range(5):
    if notas[z] >= media:
        acima = acima + 1

print(f"A média geral da sala é {media}, e a quantidade de alunos acima dessa média é {acima}")