import os
os.system("cls")

# 1 º passo - Declarar variaveis e 
# realizar a entrada de dados 

horas_por_dia = int(input("Digite quantas horas por dia você estuda: "))

if horas_por_dia <= 2:
    print("Pouco estudo")

elif horas_por_dia <= 4:
    print("Estudo médio")   

else:
    print("Muito estudo")    

