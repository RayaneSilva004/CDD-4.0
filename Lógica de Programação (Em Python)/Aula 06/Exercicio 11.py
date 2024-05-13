eleitor= int(input("Digite o total de eleitores: "))
Valido = 0
Branco = 0
Nulos = 0
soma = Valido + Branco + Nulos
while soma != eleitor:
    for x in range(eleitor):
        voto = int(input("Qual seu voto? 1 para branco, 2 para válido, 3 para nulo "))
        if voto == 1:
            Branco = Branco + 1
        elif voto == 2:
            Valido = Valido + 2
        elif voto == 3:
            Nulos = Nulos + 3
        else:
            print("Voto invalido")

porcentagemV = (Valido/eleitor)*100
porcentagemB = (Branco/eleitor)*100
porcentagemN = (Nulos/eleitor)*100

print(f"Total de votos válidos {Valido}, porcentagem é {porcentagemV}")
print(f"Total de votos brancos {Branco}, porcentagem é {porcentagemB}")
print(f"Total de votos válidos {Nulos}, porcentagem é {porcentagemN}")

