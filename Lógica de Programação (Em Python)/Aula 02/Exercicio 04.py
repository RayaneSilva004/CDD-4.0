time1 = input("Digite nome do primeiro time: ")
golstime1 = int(input("Digite os gols do  time: "))
time2 = input("Digite nome do segundo time: ")
golstime2 = int(input("Digite os gols do time: "))
if golstime1==golstime2:
    print("O Jogo entre", time1, "e", time2, "foi Empate!")
else:
    if golstime1>golstime2:
        print(time1, "Ganhou o jogo!")
    else:
        print(time2, "Ganhou o jogo!")

"""feito por mim"""