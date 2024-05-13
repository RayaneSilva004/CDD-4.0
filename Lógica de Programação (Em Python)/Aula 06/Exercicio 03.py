resp = "S"
while resp == "S":
    n = int(input("Digite um número: "))
    if n > 0:
        print("Número positivo")
    else:
        print("Número negativo")
    resp = input("Deseja realizar uma nova analise?")
