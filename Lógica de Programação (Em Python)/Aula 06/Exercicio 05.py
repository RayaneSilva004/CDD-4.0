"""num1 = int(input("Digite um número:"))
num2 = int(input("Digite um número:"))
num3 = int(input("Digite um número:"))
if num1 > num2:
    if num1 > num3:
        print(f"{num1} é maior  número")
    else:
        print(f"{num3} é o maior número")
else:
    if num2 > num3:
        print(f"{num2} é o maior número")
    else:
        print(f"{num3} é maior número")"""
ref=0
for x in range(3):
    n= int(input("Quantas atividades foram realizadas?: "))
    if n > ref:
        ref=n
print(ref)