perg1 = 0
while perg1 != 3:
    perg1 = int(input("Deseja realizar qual calculo? 1 - para triangulo e 2 para quadrado ou 3 - sair do codigo "))
    if perg1 == 1:
        btri = float(input("Digite o valor da base do triangulo: "))
        atri = float(input("Digite o valor da altura do triangulo: "))
        At = (btri * atri) / 2
        print(f"A área do triangulo é {At}")
    elif perg1 == 2:
        Lado = float(input("Digite o lado do quadrado: "))
        Aq = Lado ** 2
        print(f"A área do quadrado é {Aq}")
    elif perg1 == 3:
        print("Obrigado por usar nosso sistema")
    else:
        print("Número invalido, digite novamente")
