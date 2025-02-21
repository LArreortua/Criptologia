# Criptologia

Funcionamiento del programa
Este programa implementa el Cifrado César , uC y

Menú principal
Cifrar un mensaje
Descifrar un mensaje
Salir

El usuario elige una opción ingresando un número, y el programa se ejecuta

Cómo ejecutarlo
Compilar el código

gcc programa.c -o cifrado
Ejecutar el programa

./cifrado  # En Linux o Mac
cifrado.exe  # En Windows (CMD o PowerShell)

Cómo Funciona el Descifrado
Entrada de datos
El usuario debe ingresar:
Un mensaje en minúsculas(hola)
Una llave numérica

Proceso de Cifrado
Cada letra del mensaje se desplaza un número de posiciones determinadas por la llave, según
letra_cifrada=(letra−′𝑎′+llave+26)mod26

Un mensaje cifrado
La llave numérica usada
Proceso de Descifrado
Se revierte el
letra_descifrada=(letra−′a′ −llave+26)mod26+′a′
