soma = 0
for x in range (1,11):
    #print(f" Valor de soma: {soma} no passo {x}")
    n1 = int(input("Digite um número: "))
    if n1<0:
        #print("Achei um número ímpar")
        soma = soma + 1
print(soma)