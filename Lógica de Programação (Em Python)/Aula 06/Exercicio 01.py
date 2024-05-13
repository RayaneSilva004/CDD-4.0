att=int(input("Quantas atividades foram realizadas?: "))
soma= 0
for x in range(att):
    n1= float(input("Digite sua nota: "))
    soma = soma + n1
media= soma/att
print(media)