import os
os.system("cls")

# 1º passo - Declarar variaveis e 
# realizar a entrada de dados

idade_atual = int(input("Digite a sua idade atual: "))
ano_atual = int(input("Digite o ano atual: "))

idade_2035 = idade_atual + (2035 - ano_atual)
print("Em 2035 você terá", idade_2035, "anos: " )