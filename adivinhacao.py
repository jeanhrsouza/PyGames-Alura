print("***********************************")
print("Bem vindo no jogo de Adivinhação!")
print("***********************************")

numero_secreto = 42 #declaração de variáveis

chute_str = input("Digite o seu número: ")
# a variável que está no input é uma string. é necessário trocar para int
#para trocar para int basta fazer um casting --> chute=int(chute_str)
print("Você digitou ", chute_str)

chute = int(chute_str)

#Como fazer if. é necessário utilizar os dois pontos :
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")

print("Fim do jogo")