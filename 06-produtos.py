import os 
os.system("cls")

# 1º passo - Declarar variaveis e 
# realizar entrada de dados 

descricao = input("Digite a descrição do produto: ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco = float(input("Digite o preço utilitário do produto: "))

# 2º passo - Realizar processamento 

total = quantidade * preco

if quantidade <= 5:
    desconto = total * 0.02

elif quantidade >5 and quantidade <=10:
     desconto = total * 0.03

elif quantidade > 10: 
     desconto = total * 0.05

# 3º passo - Saída de dados 

total_a_pagar = (total - desconto) 

print("Produto:" , descricao)
print("Total sem desconto:", total)
print("Desconto:", desconto)
print("Total a pagar:", total_a_pagar)
