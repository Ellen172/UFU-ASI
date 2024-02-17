# Escreva um código em C que recebe um arquivo em texto codificação ASCII e computa as frequências de caracteres
# únicos e de pares de caracteres (2-grams). 

def calcular_caracteres(texto):
    freq = dict()

    for caracter in texto: 
        if caracter in freq.keys():
            freq[caracter] += 1
        else : 
            freq[caracter] = 1

    return freq

def calcular_pares(texto):
    freq = dict()

    for n in range(0, len(texto)-1):
        par = texto[n] + texto[n+1]

        if par in freq.keys():
            freq[par] += 1
        else : 
            freq[par] = 1
    
    return freq

def main(): 
    texto = input("Escreva seu texto cifrado em ASCII: ")

    freqCaracter = calcular_caracteres(texto)
    print("\nFrequência de cada caractere:")
    print(freqCaracter)

    print("\nFrequência de cada par de caracteres:")
    freqPares = calcular_pares(texto)
    print(freqPares)


if __name__ == "__main__":
    main()