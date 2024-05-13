nomes =["", "", "", "", "", ""]
senhas =["", "", "", "", "", ""]
resp = 0
cont = 0
while resp != 3:
    resp = int(input("Escolha sua opção\n"
                     "1 para cadastro\n"
                     "2 para login\n"
                     "3 para sair\n"))
    if resp == 1:
        for x in range(5):
            nomes[x] = input("Digite o nome de usuário: ")
            senhas[x] = input("Digite a senha do usuário: ")
    elif resp==2:
        print("Bem-Vindo ao Cadestro CDD 4.0")
        login = input("Digite o nome de usuário: ")
        senha = input(f"Olá {login}, digite a sua senha : ")
        for y in range(5):
            if login == nomes[y]:
                if senha == senhas[y]:
                    print("Login efetuado com sucesso! Bem-Vindo!")
                else:
                    print("Senha Incorreta")
            else:
                cont = cont +1
        if cont == 5:
            print("Usuário incorreto")
print("Obrigado por usar nossos serviços, até a próxima!")
