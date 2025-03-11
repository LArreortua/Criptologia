import random

# Definimos el alfabeto y sus claves binarias predefinidas asegurando mínimo 3 y máximo 10 claves por letra
CLAVES = {
    "A": ["00000000", "00000001", "00000010", "00000011", "00000100"],
    "B": ["00000101", "00000110", "00000111"],
    "C": ["00001000", "00001001", "00001010", "00001011"],
    "D": ["00001100", "00001101", "00001110"],
    "E": ["00001111", "00010000", "00010001", "00010010", "00010011", "00010100", "00010101"],
    "F": ["00010110", "00010111", "00011000"],
    "G": ["00011001", "00011010", "00011011"],
    "H": ["00011100", "00011101", "00011110"],
    "I": ["00011111", "00100000", "100001", "100010"],
    "J": ["100011", "100100", "100101"],
    "K": ["100110", "100111", "101000"],
    "L": ["101001", "101010", "101011"],
    "M": ["101100", "101101", "101110", "101111"],
    "N": ["110000", "110001", "110010", "110011"],
    "Ñ": ["110100", "110101", "110110"],
    "O": ["110111", "111000", "111001", "111010", "111011"],
    "P": ["111100", "111101", "111110"],
    "Q": ["111111", "0000000", "0000001"],
    "R": ["0000010", "0000011", "0000100", "0000101"],
    "S": ["0000110", "0000111", "0001000", "0001001"],
    "T": ["0001010", "0001011", "0001100", "0001101", "0001110"],
    "U": ["0001111", "0010000", "0010001"],
    "V": ["0010010", "0010011", "0010100"],
    "W": ["0010101", "0010110", "0010111"],
    "X": ["0011000", "0011001", "0011010"],
    "Y": ["0011011", "0011100", "0011101"],
    "Z": ["0011110", "0011111", "0100000"]
}

# Verificamos que no haya claves repetidas en diferentes letras
def verificar_unicidad():
    claves_usadas = set()
    for letra, binarios in CLAVES.items():
        for binario in binarios:
            if binario in claves_usadas:
                raise ValueError(f"Clave duplicada detectada: {binario} en la letra {letra}")
            claves_usadas.add(binario)

# Creamos el diccionario inverso para descifrar
CLAVES_INVERSAS = {binario: letra for letra, binarios in CLAVES.items() for binario in binarios}

# Función para cifrar
def cifrar(texto):
    texto = texto.upper()
    cifrado = []
    for letra in texto:
        if letra in CLAVES:
            cifrado.append(random.choice(CLAVES[letra]))
        else:
            cifrado.append(letra)  # Mantener espacios u otros caracteres sin cifrar
    return " ".join(cifrado)

# Función para descifrar
def descifrar(cifrado):
    binarios = cifrado.split()
    texto = "".join(CLAVES_INVERSAS.get(b, "?") for b in binarios)  # '?' para claves desconocidas
    return texto

# Función para mostrar el menú
def menu():
    while True:
        print("\nMenú:")
        print("1. Cifrar un mensaje")
        print("2. Descifrar un mensaje")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mensaje = input("Ingresa el mensaje a cifrar: ")
            cifrado = cifrar(mensaje)
            print("Mensaje cifrado:", cifrado)
        elif opcion == "2":
            cifrado = input("Ingresa el mensaje cifrado: ")
            descifrado = descifrar(cifrado)
            print("Mensaje descifrado:", descifrado)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Verificación de claves antes de ejecutar el programa
try:
    verificar_unicidad()
    menu()
except ValueError as e:
    print("Error en las claves:", e)
