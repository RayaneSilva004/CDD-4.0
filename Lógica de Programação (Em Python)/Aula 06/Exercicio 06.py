perg= "Sim"
while perg == "Sim" or perg =="sim":
    n= int(input("Digite um número: "))
    if n==0:
        print(f"Número Invalido, Número digitado foi {n}")
    elif n%2==0:
        print("Número par")
    else:
        print("Número ímpar")
    perg = input("Deseja realizar novamente,Sim ou Não?")
