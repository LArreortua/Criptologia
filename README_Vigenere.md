uncionamiento del programa
Este programa implementa el cifrado de Vigenère, un método de cifrado

Cómo ejecutarlo
1. Guarde el código en un archivo, por ejemplo, vigenere.py.
2. Abra la terminal o línea de comandos y ejecute el programa con:
python vigenere.py

3. Ingresa el mensaje y la clave cuando se solicita

Datos de entrada
Mensaje : S
Clave : Un

Proceso de Cifrado
1. Ajuste de la clave
La clave se ajusta para que tenga la misma longitud que el mensaje:

* Si la clave es más corta, se repite hasta igualar la longitud.
Si
Ejemplo:
Mensaje: `"ATAQUE"ATAQUE"
do"SOL"
Clave"SOLSOL"

2. Cifrado Letra por Letra
Cada l

posicion cifrada=(posicion mensaje + posicion clave)mod26

Salida del Programa:
Ingresa tu mensaje (Cualquier letra de la A a la Z, a excepción de la Ñ y sin espacios): ATAQUE
Ingresa tu clave (de la A a la Z sin espacios): SOL
Mensaje cifrado: SHLIIP
