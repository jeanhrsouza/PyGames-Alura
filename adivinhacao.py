import random

print("***********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("***********************************")

numero_secreto = random.randrange(1,101) # 0.0 - 1.0
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade ?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))
if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for rodada in range(1, total_de_tentativas + 1)  :
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue #continua com a próxima iteração

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    #Como fazer if. é necessário utilizar os dois pontos :
    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute) #abs() é para numero absoluto
        pontos = pontos - pontos_perdidos

print("Fim do jogo")

