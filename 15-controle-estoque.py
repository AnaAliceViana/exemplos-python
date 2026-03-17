import os
os.system("cls")

# 1 º passo - Declarar variaveis e 
# realizar a entrada de dados

quantidades_produtos = int(input("Digite a quantidade de produtos em estoque: "))

if quantidades_produtos < 5:
 print("Estoque baixo")

else:
 print("Estoque OK")