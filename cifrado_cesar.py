"""

Mario Ureña García

Descripción e intención del programa: Programa que cifra un mensaje usando el cifrado César

Entradas: Mensaje a cifrar y llave

Salidas: Mensaje cifrado o descifrado

"""


# Función que cifra un mensaje usando el cifrado César en base a una llave que define el número de desplazamientos, para descifrar el mensaje se debe usar la misma llave pero en negativo.


def cifrado_cesar(mensaje, llave):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra.isalpha():  # Si es una letra
            valor = ord(letra)  # Se obtiene el valor ASCII de la letra
            valor += llave  # Se desplaza el valor ASCII
            if letra.isupper():  # Si es mayúscula
                if valor > ord('Z'):  # Si se pasa del rango de letras mayúsculas
                    valor -= 26  # Se vuelve al principio
                elif valor < ord('A'):  # Si se pasa del rango de letras mayúsculas
                    valor += 26  # Se vuelve al final
            elif letra.islower():  # Si es minúscula
                if valor > ord('z'):  # Si se pasa del rango de letras minúsculas
                    valor -= 26  # Se vuelve al principio
                elif valor < ord('a'):  # Si se pasa del rango de letras minúsculas
                    valor += 26  # Se vuelve al final
            mensaje_cifrado += chr(valor)
        else:  # Si no es una letra entonces se añade tal cual
            mensaje_cifrado += letra
    return mensaje_cifrado


# Main
mensaje = input("Introduzca el mensaje a cifrar: ")
llave = int(input("Introduzca la llave: "))
print("El mensaje cifrado es: ", cifrado_cesar(mensaje, llave))
