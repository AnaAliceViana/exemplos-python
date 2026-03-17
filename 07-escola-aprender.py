import os
os.system("cls")

# 1º passo - Declarar variaves e 
# realizar entrada de dados 

nivel = int(input("Digite seu nível: "))
aulas_semana = int(input("Digite a quantidade de aulas por semana: "))

if nivel == 1:
    valor_hora = 12

if nivel == 2: 
   valor_hora = 17 

if nivel == 3:
    valor_hora = 25

salario = aulas_semana * valor_hora * 4     

print("Sálario final é: ", salario)