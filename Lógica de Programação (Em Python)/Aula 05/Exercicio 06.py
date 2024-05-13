nome=["","","","","","",]
senha=["","","","","","",]
for x in range (5):
    nome[x]= input("Digite o nome de usuário: ")
    senha[x]= int(input("Digite a senha: "))
for y in range (5):
    print(f"Usuário {nome[y]}, senha {senha[y]},{y}")