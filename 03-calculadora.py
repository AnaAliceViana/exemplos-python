import os 
os.system("cls")

# 1º passo - Declarar variaveis e
# realizar entrada de dados 

print ("Bem Vindo a Calculadora Virtual")

numero01 = float(input("Digite um número: "))
numero02 = float(input("Digite outro número: "))

operacao = input ("Escolha a operação: ")

#SE
if (operacao == "+"): 
     resultado = numero01 + numero02

#SENAO SE 
elif (operacao == "-"):
     resultado = numero01 - numero02

elif (operacao == "*"):
     resultado = numero01 * numero02   
    
elif (operacao == "/"):
     resultado = numero01 / numero02 

print ("Seu resultado é:", resultado)

