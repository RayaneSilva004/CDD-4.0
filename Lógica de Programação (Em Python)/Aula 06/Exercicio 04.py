ano = int(input("Em que ano estamos? "))
mes = int (input("Digite em número o mes que estamos: exemplo 1 para janeiro: "))
idade = int(input("Digite sua idade: "))
mes1 = int(input("Digite em número o mes que nasceu: exemplo 1 para janeiro: "))
AN = ano-idade
if mes < mes1:
    print(AN-1)
else:
    print(AN)