A = [0,0,0,0,0,0,0,0,0,0]
M = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
    A[x]= int(input("Digite um número: "))
print(A)
X= int(input("Digite mais um número: "))
for y in range(10):
    M[y] = A[y] * X
print(M)