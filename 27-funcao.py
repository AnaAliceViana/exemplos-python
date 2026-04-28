import os
os.system ("cls")

def escreva(): 
     print("Olá mundo")
    

#criando função com parametro
def exibir_dados(nome, idade, email):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Email:{email}")
    print("=" * 100)

# Criando uma função com retorno
def somar(num1, num2):
     resultado = num1 + num2 
     return resultado 


#chamando a função
escreva() 

#chamando função exibir_dados
exibir_dados("Caio",40,"Caio@gmail.com")
exibir_dados("Rebeca",40,"Caio@gmail.com")


# Chamndo a função com retorno 
total = somar(10,20)
print(f"O total será: {somar(10,20)}")