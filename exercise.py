lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2,12,12, 3, 3, -52]

media = 0
ocorre1 = 0
pares = []
maxv = lista[0]
minv = lista[0]
somaniga = 0

for achar in range(0, len(lista)):
    
    if (maxv < lista[achar] ) :
       maxv = lista[achar]   
        
    if (lista[achar] < minv):
       minv = lista[achar]
       
    if (lista[achar]% 2 == 0):
        pares.append(lista[achar])
        
    if (lista[achar] == lista[0]):
        ocorre1 = ocorre1 + 1
        
    if (lista[achar] < 0):
        somaniga = somaniga + lista[achar]
        
        
    media =+ media + lista[0]
    
media = media / len(lista)
print("O valor máximo da lista é" ,maxv)
print("O valor minimo da lista é",minv)
print("Os números pares são", pares)
print("O primeiro número da lista aparece {} vezes" .format(ocorre1))
print("A média é", media)
print("A soma dos números negativos são", somaniga)
