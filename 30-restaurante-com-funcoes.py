import os
os.system("cls")

def dividir_conta(valor_total, quantidade_pessoas):
    resultado = valor_total / quantidade_pessoas
    return resultado

print("Seja Bem-Vindo ao App Minha Conta")

valor_total = float(input("Informe o valor total da conta: "))
quantidade_pessoas = int(input("Informe a quantidade de pessoas: "))

print("=== Pressione Enter para Calcular ===")

print(f"O valor será de: {dividir_conta(valor_total, quantidade_pessoas)}")