
def primo(rem,prim):
     num=0
     for i in range(-prim,0):
           f = rem %  prim
           prim -= 1
      
           if f == 0:
               num += 1
     if num == 2:  
            print("{}, esse numero é primo".format(rem))
      
     else:
        print("{}, esse numero não é primo".format(rem))
        
#Escolhendo as variaveis fora da funcao para serem utilizadas dentro dela
prim = int(input("Fale seu numero:\n"))

rem = prim
 
primo(rem,prim)