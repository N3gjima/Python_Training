import random

chute= 0
golgole = 0
golepega = 0
golchute = 0

while (golchute < 4 and golgole < 4):
   print("\n####################")
   print("  You: {} X PC: {}".format(golchute,golgole))
   print("_____________________\n|        O          |\n|       -|-         |\n|       / \         |")
   golepega=random.randint(1,3)
   chute=int(input("Adivinhe o número, se acertar, você fará o gol!\nescolha um número de 1 até 3\n"))
   print("O goleiro se jogou em: {}".format(golepega))
   if (golepega == chute and chute <= 3):
      golgole += 1
      print("################")
      print("\nQue defessaaaaa!")
  elif():
      golchute += 1
      print("#############")
      print("Gooooooolllll")
if golchute == 4:
        print("####################")
        print("Você fez:",golchute, "gols")
        print("Parabens, voce ganhou o jogo!!!!")
elif golgole == 4:
        print("####################")
        print("O goleiro pegou:",golgole,"gols")
        print("Você perdeuuu!!!")
        
   
   
   
    
    