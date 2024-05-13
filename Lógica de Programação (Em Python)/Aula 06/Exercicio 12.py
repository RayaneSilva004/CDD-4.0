horainicial = int(input("Digite a hora que começou o jogo de xadrez: "))
horafinal = int(input("Digite a hora que terminou o jogo de xadrez: "))
if horainicial <= horafinal:
  duracao = horafinal - horainicial
else:
  duracao = 24 - (horainicial - horafinal)
print(duracao)