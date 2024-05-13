Dentro = 0
Fora = 0
for x in range (1,11):
    n1 = int(input("Digite um número: "))
    if n1 >=10 and n1<=20:
        print("achei um dentro od intervalo")
        Dentro = Dentro + 1
    else:
        print("Achei um fora do intervalo")
        Fora = Fora +1
print(f"Dentro do intervelo tem {Dentro} números e fora do intervalo tem {Fora} números" )