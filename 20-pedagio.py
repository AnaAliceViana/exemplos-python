import os
os.system("cls")

# 1 º passo - Declarar variaveis e 
# realizar a entrada de dados 

veiculo = (input("Digite o tipo de veículo: "))

if veiculo == "Carro":
    print ("O valor do pedágio correspondente a R$10")

elif veiculo == "Moto":
    print ("O valor do pedágio correspondente a R$5")

elif veiculo == "Caminhão":
    print ("O valor do pedágio correspondente a R$20")

else:
    print ("Tipo inválido")