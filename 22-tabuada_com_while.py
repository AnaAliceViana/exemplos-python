import os 
os.system("cls")

numero = int(input("Digite um número: "))
limite = int(input("Digite o limite da sua tabuada: "))
contador = 0 

while(contador <= limite):
    print(f"{numero} x {contador} = {numero * contador}")
    contador+=1