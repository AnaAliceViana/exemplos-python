
# 1º passo - Declarar variaveis e 
#realizar entrada de dados 

print("Seja Bem vindo ao Boletim Virtual")

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
nota03 = float(input("Digite a terceira nota: "))

# 2º passo - Processamento 
media = (nota01 + nota02 + nota03) /3 

#3 passo - Exibir a saída (resultado)
print("A sua média foi: " , media )

if(media>=7):
    print("Você foi APROVADO!")

elif(media>=4 and media <=6):
    print("Você está de RECUPERAÇÃO!")

else:
    print("Você foi REPROVADO!")    