print("***********************************")
print("Bem vindo no jogo de Adivinhação!")
print("***********************************")

numero_secreto = 42 #declaração de variáveis
total_de_tentativas = 3



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
        print("Você acertou")
        break
    else:
        if(chute_maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(chute_menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")


print("Fim do jogo")

