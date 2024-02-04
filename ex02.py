# Decifrar mensagens que utilizam cifra de Verne
# Recebe uma lista com mensagens cifradas (todos do mesmo tamanho) que utilizaram a mesma chave

def transformar_lista_chave(lista):
    chave = ""
    for key in lista: 
        chave += hexar_numero(key[0]) + hexar_numero(key[1])
    return chave

def dec_correta(lista_letras): 

    if lista_letras == "-":
        return False

    for letra in lista_letras: 
        if (ord(letra) != 32) and (ord(letra) not in range(65, 91)) and (ord(letra) not in range(97, 123)):
            return False

    return True

def hexar_numero(number):
    if number == 10:
        return 'A'
    elif number == 11:
        return 'B'
    elif number == 12:
        return 'C'
    elif number == 13:
        return 'D'
    elif number == 14:
        return 'E'
    elif number == 15:
        return 'F'
    else : return str(number)

def numerar_hexa(text):
    if text=='A' or text=='a':
        return 10
    elif text=='B' or text=='b':
        return 11
    elif text=='C' or text=='c':
        return 12
    elif text=='D' or text=='d':
        return 13
    elif text=='E' or text=='e':
        return 14
    elif text=='F' or text=='f':
        return 15
    else : return int(text)

def busca_espaco(lista_letra, key1, key2): 

    for a in range(0, len(lista_letra)):
        for b in range(a+1, len(lista_letra)):

            niblle1_p1 = numerar_hexa(lista_letra[a][0])
            niblle1_p2 = numerar_hexa(lista_letra[a][1])

            niblle2_p1 = numerar_hexa(lista_letra[b][0])
            niblle2_p2 = numerar_hexa(lista_letra[b][1])

            dif = int(niblle1_p1) ^ int(niblle2_p1)

            if dif in range(4,8): 
                key1.append(niblle1_p1 ^ 2)
                key1.append(niblle1_p2)
                key2.append(niblle2_p1 ^ 2)
                key2.append(niblle2_p2)

                return 0


def main() :

    lista_msg = []
    lista_dec1 = []
    lista_dec2 = []

    msg = input("Insira as mensagens que deseja (aperte enter com mensagem vazia para terminar)\n")
    while msg != "": 
        lista_msg.append(msg)
        msg = input() 

    list_key1 = []
    list_key2 = []

    tam_msg = len(lista_msg[0])
    nro_msg = len(lista_msg)
    
    for n in range(0, tam_msg, 2): # todas as mensagens devem ter o mesmo tamanho

        lista_letra = []

        # criar lista com as letras (dois caracteres) de cada mensagem
        for msg in lista_msg: 
            lista_letra.append(msg[n] + msg[n+1])
            
        key1 = []
        key2 = []
        busca_espaco(lista_letra, key1, key2)

        list_key1.append(key1)
        list_key2.append(key2)

        if key1 == []: 
            # não foi encontrado o espaço 
            lista_dec1.append("-")
            lista_dec2.append("-")

        else : 
            
            msg_dec1 = []
            msg_dec2 = []

            for letra in lista_letra: 

                niblle1 = numerar_hexa(letra[0])
                niblle2 = numerar_hexa(letra[1])
                
                # teste chave 1
                dec1 = []
                dec1.append(key1[0] ^ niblle1)
                dec1.append(key1[1] ^ niblle2)

                nro_dec1 = (dec1[0] * 16) + dec1[1] # transforma hexa em decimal
                msg_dec1.append(chr(nro_dec1)) # transforma decimal em letra (ascii)
           
                # teste chave 2
                dec2 = []
                dec2.append(key2[0] ^ niblle1)
                dec2.append(key2[1] ^ niblle2)

                nro_dec2 = (dec2[0] * 16) + dec2[1] # transforma hexa em decimal
                msg_dec2.append(chr(nro_dec2)) # transforma decimal em letra (ascii)

            lista_dec1.append(msg_dec1)
            lista_dec2.append(msg_dec2)

    
    key_final = []
    list_msg_final = []
    for x in range(0, nro_msg):
        list_msg_final.append("")
    
    for x in range(0, tam_msg//2):

        if(dec_correta(lista_dec1[x])):
            key_final.append(list_key1[x])
            for y in range(0, len(lista_dec1[x])):
                list_msg_final[y] += lista_dec1[x][y]

        elif(dec_correta(lista_dec2[x])):
            key_final.append(list_key2[x])
            for y in range(0, len(lista_dec2[x])):
                list_msg_final[y] += lista_dec2[x][y]

        else : 
            key_final.append("--")
            for y in range(0, len(list_msg_final)):
                list_msg_final[y] += "-"



    print("Chave : " + transformar_lista_chave(key_final))

    print("\nMensagens finais: \n")
    for mensagem_dec in list_msg_final:
        print(mensagem_dec)



if __name__ == "__main__":
    main()