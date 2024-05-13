secreto= 12345
c = 0
senha = int(input("Digite sua senha: "))
c= 1
while senha != secreto:
    c=c+1
    senha= int(input("Senha Incorreta, digite novamente"))
    if c == 3 and senha != secreto:
        print("Acesso Bloqueado por uso de senha incorreta")
        break
if senha == secreto:
    print("Acesso Liberado")