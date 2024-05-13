resp = "sim"
while resp == "sim":
    nota1 = float(input("Digite primeira nota"))
    while nota1 < 0 or nota1 > 10:
        print("Número deve ser entre 0 e 10")
        nota1 = float(input("Primeira nota inválida digite novamente"))
    nota2 = float(input("Digite segunda nota"))
    while nota2 < 0 or nota2 > 10:
        print("Número deve ser entre 0 e 10")
        nota2 = float(input("Segunda nota inválida, digite novamente"))
    media = (nota1 + nota2)/2
    print(media)
    resp = input("Deseja realizar novo calculo? sim/não")