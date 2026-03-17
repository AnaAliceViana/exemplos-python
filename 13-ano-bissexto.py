import os 
os.system("cls")

# 1º passo - Declarar variaveis e 
# realizar a entrada de dados

ano = int(input("Digite o ano: "))

if ano % 4 == 0:
    print("Ano bissexto")

else:
    print("Não é bissexto")    