perg = "Sim"
while perg == "Sim" or perg =="sim":
    btri= float(input("Digite o valor da base do triangulo: "))
    atri= float(input("Digite o valor da altura do triangulo: "))
    A = (btri * atri)/2
    print(f"A área do triangulo é {A}")
    perg = input("Deseja realizar novamente,Sim ou Não?")