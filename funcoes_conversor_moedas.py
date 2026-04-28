import os 
os.system("cls")

#Criando as funções 
#Criando a função que exibe o menu
def exibir_menu():
    print("=== Conversor de Moedas ===")
    print("[1] - Converter DOLAR -> REAL")
    print("[2] - Converter REAL -> DOLAR")
    print("[3] - Sair")

def limpar_tela():
    os.system("cls")   

#Função Coverter de dólar para real
def converter_dolar_para_real(quantia_dolar, cotacao):
    total_reais = quantia_dolar * cotacao
    return total_reais 

#Função Converter Real para Dolar 
def converter_real_para_dolar(quantia_real, cotacao):
    total_dolares = quantia_real / cotacao 
    return total_dolares

#Função Sair 
def sair():
    exit()