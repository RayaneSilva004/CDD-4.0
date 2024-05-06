tipo = input("Qual o tipo de combustível? G para Gasolina e E para Etanol. ")
litros = float(input("Quantos litros foram vendidos? "))
E = 4.90 * litros
G = 5.80 * litros
if tipo == "G" or "g":
    print(f"O valor a ser pago é", G,"reais")
else:
    print(f"O Valor a ser pago é", E,"reais")
