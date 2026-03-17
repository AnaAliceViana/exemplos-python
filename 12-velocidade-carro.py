import os
os.system("cls")

# 1 º passo - Declarar variaveis e 
# realizar a entrada de dados 


velocidade = float (input("Digite a velocidade do carro: "))

if velocidade > 80:
    print ("Multado")

else:
    print ("Dentro do limite")