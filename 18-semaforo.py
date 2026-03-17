import os
os.system("cls")

# 1 º passo - Declarar variaveis e 
# realizar a entrada de dados

cor = input ("Digite a cor de um semáforo: ")

if cor == "Verde":
    print ("Pode passar")

elif cor == "Amarelo": 
    print ("Atenção")

elif cor == "Vermelho":
    print ("Pare")

else:
    print ("Cor inválida")