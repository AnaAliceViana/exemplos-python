import os
os.system("cls")

print("Seja Bem-Vindo ao Caixa Eletrônico")

saldo = 1000
escolha = "Sair"

while escolha == "Sair":
    escolha = input("Selecione a opção para prosseguir: ")

    print("\n== Caixa Eletrônico ===")
    print("Saldo")
    print("Depósito")
    print("Sacar")
    print("Sair")

    if escolha == "Saldo":
        print(f"Seu saldo é {saldo}")

    elif escolha == "Depositar":
        valor = float(input("Qual valor você deseja depositar?: "))
        input(f"Você confirma depositar esse valor? {valor}")
        print("Depósito feito!")
        
    elif escolha == "Sacar":
        valor = input("Digite o valor que você deseja sacar")   
        if valor: 
             valor = float(valor)
             if valor <= saldo:
                 saldo -= valor 
                 print(f"Saque realizado! Saldo atual: rs{saldo}")
             else: 
               print("Saldo insuficiente!")  
        else: 
            print("Valor inválido! Digite apenas número")
    elif escolha == "Sair":
        print("Saindo do programa!")
    break