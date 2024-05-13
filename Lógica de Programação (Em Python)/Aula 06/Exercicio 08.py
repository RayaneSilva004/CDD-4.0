n = int(input("Quantos números precisa tirar a média? "))
soma = 0
for x in range(n):
    num = int(input("Digite um número: "))
    soma = soma + num
media = soma/n
print(f"A soma dos números é {soma} e a media dos números é: {media}")
