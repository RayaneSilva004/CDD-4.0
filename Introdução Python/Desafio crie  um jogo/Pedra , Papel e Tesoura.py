def jogar():
  print("Bem vindo ao pedra, papel e tesoura!")
  opcoes = ["pedra", "papel", "tesoura"]
  vitoriaPlayer1 = 0
  vitoriaPlayer2 = 0

  while vitoriaPlayer1 <2 and vitoriaPlayer2 <2:
    escolha1 = input("Faça sua escolha player 1: \n-pedra\n-papel\n-tesoura: ").lower()
    validar_escolha(escolha1)
    escolha2 = input("Faça sua escolha player 2: \n-pedra\n-papel\n-tesoura: ").lower()
    validar_escolha(escolha2)

    if escolha1 == escolha2:
      print("Empate!")
    elif (escolha1 == "pedra" and escolha2 == "tesoura") or (escolha1 == "papel" and escolha2 == "pedra") or (escolha1 == "tesoura" and escolha2 == "papel"):
          print("Player 1 venceu a rodada")
          vitoriaPlayer1 += 1
    else:
      print("Player 2 venceu a rodada")
      vitoriaPlayer2 += 1

    print(f"Placar: Player 1 - {vitoriaPlayer1} | Player 2 - {vitoriaPlayer2}")

  if vitoriaPlayer1 > vitoriaPlayer2:
    print("Player 1 venceu a partida!")
  if vitoriaPlayer1 == vitoriaPlayer2:
    print("A partida terminou em empate")
  else:
    print("Player 2 venceu a partida!")
  verificar_jogar_novamente()

def validar_escolha(escolha):
    opcoes = ["pedra", "papel", "tesoura"]
    while escolha not in opcoes:
        print("Esolha inválida, tente novamente")
        escolha = input("Escolha pedra, papel ou tesoura: ").lower()
    return escolha

def verificar_jogar_novamente():
  jogar_novamente = input("Desejam jogar novamente? \n-sim\n-não)").lower()
  if jogar_novamente == "sim"  :
    jogar()
  else:
    print("Obrigado por jogar, até mais!")

jogar()
