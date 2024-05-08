n1 = float(input("Nota primeira atividade: "))
n2 = float(input("Nota segunda atividade: "))
n3 = float(input("Nota terceira atividade: "))

media = (n1+n2+n3)/3

if media>=7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
