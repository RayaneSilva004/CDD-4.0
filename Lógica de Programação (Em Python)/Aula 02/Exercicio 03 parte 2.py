n1 = float(input("Nota da primeira atividade: "))
n2 = float(input("Nota da segunda atividade: "))
n3 = float(input("Nota da terceira atividade: "))
media = (n1+n2+n3)/3
if media>=7:
    print("Aluno Aprovado")
else:
    if media<4:
        print("Aluno Reprovado")
    else:
        print("Aluno em Recuperação")
