NUMEROS= [0,0,0,0,0]
for x in range(5):
    NUMEROS[x]= int(input("Digite um número: "))
print(NUMEROS)
for y in range(4,-1,-1):
    print(NUMEROS[y], end =" ")