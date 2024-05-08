tipo = input("Qual o tipo de combustível? G para Gasolina e E para Etanol. ")
litros = float(input("Quantos litros foram vendidos? "))
E = 4.90
G = 5.80
if tipo == "G"or"g":
    total = G*litros
elif tipo == "E"or"e":
    total = E*litros
else:
    print("Tipo de combustivel inválido")
print(f"Você gastou", total, "reais")