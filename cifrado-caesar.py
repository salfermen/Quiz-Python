print("Ingresa el mensaje cifrado")
mensajeCifrado = input()
print("Cuántas veces se movió la letra para cifrar")
veces = int(input())

mensajeOriginal = ""

for i in range(len(mensajeCifrado)):
    letra = mensajeCifrado[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')

    if not (minuscula or mayuscula):
        mensajeOriginal += letra  # Mantener caracteres que no son letras.
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')

        # Decodificar: Restar la cantidad de veces y ajustar para no ser negativo.
        nuevoAscii = (ascii - baseAscii - veces + 26) % 26 + baseAscii
        nuevaLetra = chr(nuevoAscii)
        mensajeOriginal += nuevaLetra

print("Mensaje original:", mensajeOriginal)
