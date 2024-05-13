hora01 = int(input("Digite a hora da primeira entrada: "))
minuto01 = int(input("Digite os minutos da primeira entrada: "))
hora02 = int(input("Digite a hora da segunda entrada: "))
minuto02 = int(input("Digite os minutos da segunda entrada: "))
if hora01 > 12:
    hora01 = hora01 - 12
if hora02 > 12:
    hora02 = hora02 - 12
horaT = hora01 + hora02
minutoT = minuto01 + minuto02
if minutoT >= 60:
    minutoT = minutoT - 60
    horaT = horaT + 1
print(f"{horaT}:{minutoT}")