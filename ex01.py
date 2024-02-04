# Implementar operações ENC e DEC da Cifra de Vigenére (com XOR). 
# A operação ENC recebe do usuário um texto em claro e chave (em ascii) e produz texto cifrado em ASCII representando o hexa do texto cifrado. 
# A operação DEC recebe do usuário um texto cifrado (ascii do hexa) e uma chave secreta (em ascii) e produz o texto em claro. 

import sys

def exibir_menu():
    print("\nMenu:")
    print("1. Operação ENC")
    print("2. Operação DEC")
    print("3. Sair")

def encriptar():

    print("\n---- Operação ENC ----")
    mensagem = input("Insira a mensagem que deseja encriptar: ")
    chave = input("Adicione a chave da encriptação (em ASCII): ")

    # xor com a chave
    result = [] 
    for letra in mensagem: 
        ascii = ord(letra)
        result.append(ascii ^ int(chave))

    cifrado = ""
    for num in result: 
        cifrado += chr(num)

    print("\nResultado: " + cifrado)

def desencriptar():
    
    print("\n---- Operação DEC ----")
    mensagem = input("Insira a mensagem que deseja desencriptar: ")
    chave = input("Adicione a chave da encriptação (em ASCII): ")

    # xor com a chave
    result = [] 
    for letra in mensagem: 
        ascii = ord(letra)
        result.append(ascii ^ int(chave))

    texto = ""
    for num in result: 
        texto += chr(num)

    print("\nResultado: " + texto)

def main():
    while True:
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            encriptar()
        elif opcao == "2":
            desencriptar()
        elif opcao == "3":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()