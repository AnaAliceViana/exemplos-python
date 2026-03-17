import os
os.system("cls")

# 1º passo - Declarar as variaveis e
# realizar a entrada de dados

nome = input("Digite o seu nome de usuário: ")
senha = int(input("Digite a senha: "))

if nome == "admin" and senha == 123:
    print("Acesso LIBERADO!")

else:
    print("Acesso NEGADO!")   