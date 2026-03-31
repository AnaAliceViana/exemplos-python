import os 
os.system("cls")

print("Exemplo Habilitação com o While")

resposta = "sim"

while(resposta == "sim"):

    nome = input("Digite seu nome: ")
    idade = int(input("Digite qual é a sua idade: "))

    if idade >=18:
        habilitacao = int(input("Você possui habilitação? (1-Sim ou 2-Não): "))

        if habilitacao == 1:
         print("Você pode dirigir!")    

        else:
         print("Você não possui habilitação!")

    else:
     print("Você é menor de idade!")

    resposta = input("Você gostaria de exercer novamente? (sim ou não): ")
print("Fim de Programa, espero ter ajudado!")

        