print("***********************************")
print("Bem vindo no jogo de Adivinhação!")
print("***********************************")

numero_secreto = 42 #declaração de variáveis

chute_str = input("Digite o seu número: ")
# a variável que está no input é uma string. é necessário trocar para int
#para trocar para int basta fazer um casting --> chute=int(chute_str)
print("Você digitou ", chute_str)

chute = int(chute_str)


acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

#Como fazer if. é necessário utilizar os dois pontos :
if(acertou):
    print("Você acertou")
else:
    if(chute_maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(chute_menor):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo")