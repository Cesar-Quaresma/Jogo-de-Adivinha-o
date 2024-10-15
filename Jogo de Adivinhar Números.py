print("\033[0:33m  Nessa brincadeira aqui, você participará do \033[1:32m'Jogo da Adivinhação'\033[0:33m, no qual você precisará acertar, ou melhor, você \nadivinhará o número em que o 'Computador' o escolhera sendo o mostrado na tela.")
print("\033[0:33m  Em um total de \033[0:32m'9(nove) tentativas'\033[0:33m, 'você \033[1:39m(Jogador)\033[0:33m' acumulará um total de acertos sendo esses somados igualmente \naos do seu rival, o \033[1:35m'Computador'\033[0:33m, que juntos disputarão quantos os foram somados!")
print("\033[0:32m  Terão apenas 9(nove) tentativas. Quêm acumulará um total de vitórias maior em relação ao outro, será o 'Vencedor'!! \033[1:34m\n BOA SORTE:")

vitjogador = 0
vitpc = 0

from random import randint
for c in range (1,10):
    jogador = int(input("\033[1:39m'Jogador'\033[0:33m, faça a sua jogada: "))
    computador = randint(1,9)
    if jogador == computador:
        print(f'\033[1:39m"Jogador Acertou!!" \033[0:39madivinhou, digitando: \033[1:39m{jogador}, \033[0:39me o \033[1:35m"Computador" \033[0:39mdigitou: \033[1:35m{computador}')
        vitjogador += 1
    elif jogador != computador:
        print(f'"\033[1:31mJogador Errou"\033[0:39m, ora digitando: \033[1:39m{jogador}, \033[0:33me o \033[1:35m"Computador" \033[0:39mpor sua vêz o digitou: \033[1:35m{computador}.')
        vitpc += 1
if vitjogador > vitpc:
       print(f"\033[1:34m  PARABÊNS,Você VENCEU!!\033[0:39m Você, o \033[1:39m'Jogador' \033[0:39mdigitou \033[1:35m{vitjogador}, e 'Computador' com \033[1:35m{vitpc}. ")
else:
    if vitpc > vitjogador:
      print(f"\033[1:35m \n Infelizmente Você PERDEU!!\033[0:39m Você \033[1:39m'Jogador' \033[0:39mteve \033[1:39m{vitjogador} acerto(s)\033[0:39m, porém você não 'adivinhou', segundo os 9 números escolhidos \npelo \033[1:35m'Computador'\033[0:39m: cerca de \033[1:35m{vitpc}\033[0:39m números. \033[1:34m \n Tente novamente!")

