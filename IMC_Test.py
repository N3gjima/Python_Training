p = input("Qual o seu peso ?(kg)\n")
a = input("Qual a sua altura? (m)\n")
peso = float(p)
altura =float(a)
imc =(peso / (altura ** 2)) 
print(" Seu IMC é:\n{:.2f}".format(IMC))
if (imc >= 18.5 and imc < 25):
    print("Você está no peso ideal ")
else:
    print("Cuide do seu corpo, puta")