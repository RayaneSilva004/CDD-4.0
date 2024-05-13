att=int(input("Quantas atividades foram realizadas?: "))
if att < 0:
    print("Número de atividades invalida")
soma = 0
for x in range(att):
    n1 = float(input("Digite a nota da atividade: "))
    if n1 > 10 or n1 < 0:
        print("Nota Invalida ")
    soma = soma + n1
    media = soma/att
if media >= 7:
    print(f"Aluno foi Aprovado, a media foi: {media}")
elif media >= 4:
    print(f"Aluno está Recuperação, a media foi: {media}")
else:
    print(f"Aluno foi Reprovado, a media foi: {media}")