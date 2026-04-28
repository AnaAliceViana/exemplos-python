import os 
os.system("cls")

def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def subtrair(numero1, numero2):
    resultado = numero1 - numero2 
    return resultado

def multiplicar(numero1, numero2):
    resultado = numero1 * numero2 
    return resultado 

def dividir(numero1, numero2):
    resultado = numero1 / numero2 
    return resultado

def encerrar_programa():
    print("Operação Inválida")
    input("Pressione Enter para finalizar...")
    exit()

print("Seja Bem-Vindo a super Calculadora 2.0 pro max")

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

print("Escolha uma das opções abaixo:")
print("[1] - Somar")
print("[2] - Subtarir")
print("[3] - Multiplicar")
print("[4] - Dividir") 
opcao = int(input("Escolha uma opção: "))

if(opcao == 1):
    #Chamar a função somar 
    print(f"A soma é: {somar(numero1, numero2)}")
elif(opcao == 2):
    #Chamar a função subtrair
     print(f"A subtração é: {subtrair(numero1, numero2)}")
elif(opcao == 3):
    #Chamar a função multiplicar 
    print(f"A multiplicação é: {multiplicar(numero1, numero2)}")
elif(opcao == 4):
    #Chamar a função multiplicar 
    print(f"A divisão é: {dividir(numero1, numero2)}")    

else:
    #Chamar a função operação inválida
    encerrar_programa()
