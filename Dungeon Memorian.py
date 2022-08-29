import random
vida = 10
dano = 1
print("#####################")
print("##Dungeon Memorian###")
print("#####################")

nickname =input("\nDigite seu nome Guerreiro!\n")
print("-------------")
print("|", nickname,"\n| Life:",vida,"\n| Dano:",dano, "\n")
print("{} se depara com um caminho trifurcado a frente, o que {} faz ?".format(nickname,nickname))
print("<-- Esquerda ^ Frente ^ Direita -->")
direcao=input("Então {} levanta e se depara com um caminho trifurcado.\nQual direção você escolhe?\n###################################\n".format(nickname,nickname))
    
if (direcao == "esquerda" or direcao == "Esquerda"):
    vida = vida + 1
    print("{} anda por alguns metros\naté que escorrega numa poça de lama,\nsua cor era muito diferente de uma lama normal,\n{} se sente revigorado e feliz.\n{} agora tem cabelo\n#####################################\n" .format(nickname, nickname, nickname))
      
    print("-------------")        
    print("|", nickname,"\n| Life:",vida,"\n| Dano:",dano, "\n")
    if (direcao == "esquerda" or direcao == "Esquerda"):
          direcao=input("{} se levanta com alegria e cabelo porém começa a feder, o que {} fará, há alguns arbustos, um lago e uma velha senhora catando algumas frutas por perto, o que {} fará ?\n ".format(nickname,nickname,nickname))
          if direcao == "arbustos" or direcao=="Arbustos":
              vida = vida - 11
              print("{} caiu em arbustos venenosos, {} morreu\n".format(nickname,nickname))
              print("|", nickname,"\n| Life:",vida,"\n| Dano:",dano, "\n")
          
          
elif (direcao == "direita" or direcao == "Direita"):
         print("{} vê homens amarelos seguindo a sua frente\neles deixam cair uma enorme espada negra\n{} grita contudo eles não ouvem\n{} resolveu pegar a espada para si, para devolver se os encontrasse de novo ou não\n##################################".format(nickname,nickname,nickname))
        
elif(direcao == "frente" or direcao== "Frente"):
           vida = vida - 10
           print("O caminho a frente encheu {} de determinação\nUm caminho reto é bom\nporém {} pisa numa faca enfurrajada\n{} morre de tetano\n##################################".format(nickname,nickname,nickname))
           print("{}\nLife: {}\nDamage: {}".format(nickname,vida,dano))
        
