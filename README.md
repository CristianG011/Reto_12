# Reto_12
### Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.
### endswith
Es una función de manipulación de series de caracteres que manipula todos los tipos de datos (BIT, BLOB y CHARACTER) y devuelve un valor booleano para indicar si una serie de caracteres finaliza por otra.

https://www.ibm.com/docs/es/integration-bus/10.0?topic=functions-endswith-function#:~:text=ENDSWITH%20es%20una%20funci%C3%B3n%20de,de%20caracteres%20finaliza%20por%20otra.
### startswith
Indica si una cadena de texto comienza con los caracteres de una cadena de texto concreta, devolviendo true o false según corresponda.

https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith#:~:text=El%20m%C3%A9todo%20startsWith()%20indica,true%20o%20false%20seg%C3%BAn%20corresponda.
### isalpha
Es una función incorporada que se utiliza para verificar si una cadena contiene únicamente caracteres alfabéticos (letras) y no está vacía. Devuelve True si todos los caracteres en la cadena son letras, de lo contrario, devuelve False .

https://thedataschools.com/python/strings/isalpha-metodo-string/#:~:text=El%20m%C3%A9todo%20isalpha()%20en,de%20lo%20contrario%2C%20devuelve%20False%20.
### isalnum
Comprueba si la cadena es alfanumérica, es decir, si los caracteres que la componen son solo letras y/o números y tiene al menos un carácter. Devuelve True en caso afirmativo. Devuelve False si no es alfanumérica o está vacía.

https://techkrowd.com/programacion/python/python-metodos-de-cadenas-ii/#:~:text=El%20m%C3%A9todo%20isalnum%20comprueba%20si,es%20alfanum%C3%A9rica%20o%20est%C3%A1%20vac%C3%ADa.
### isdigit
devuelve un valor booleano True o False si coincide que la cadena contenga caracteres dígitos.

https://platzi.com/discusiones/1104-python/77148-para-que-sirve-el-metodo-isdigit/#:~:text=La%20funci%C3%B3n%20isdigit()%20devuelve,la%20cadena%20contenga%20caracteres%20d%C3%ADgitos.
### isspace
omprueba si todos los caracteres de la cadena son espacios en blanco. Se entiende por espacio en blanco los espacios, tabulaciones y retornos de carro. Devuelve True en caso afirmativo, y False si contiene algún otro tipo de carácter o la cadena está vacía.

https://techkrowd.com/programacion/python/python-metodos-de-cadenas-ii/#:~:text=isspace(),o%20la%20cadena%20est%C3%A1%20vac%C3%ADa.

### istitle
es un método de cadena (string) que se utiliza para verificar si una cadena tiene un formato de título. Una cadena se considera que está en formato de título si todas las palabras en la cadena comienzan con una letra mayúscula y el resto de las letras son minúsculas.

https://thedataschools.com/python/strings/istitle-metodo-string/#:~:text=El%20m%C3%A9todo%20istitle()%20en,de%20las%20letras%20son%20min%C3%BAsculas.

### islower
devuelve True si todos los caracteres de una cadena están en minúsculas, False en caso contrario.

https://j2logo.com/python/convertir-a-mayusculas-y-minusculas-en-python/#:~:text=islower()%20devuelve%20True%20si,min%C3%BAsculas%2C%20False%20en%20caso%20contrario.

### isupper
devuelve True si todos los caracteres de una cadena están en mayúsculas, False en caso contrario.

https://j2logo.com/python/convertir-a-mayusculas-y-minusculas-en-python/#:~:text=isupper()%20devuelve%20True%20si,may%C3%BAsculas%2C%20False%20en%20caso%20contrario.

# Procesar el archivo y extraer:

### Cantidad de vocales
### Cantidad de consonantes
### Listado de las 50 palabras que más se repiten
```python

from collections import Counter

with open("mbox-short.txt", "r", encoding="utf-8") as ms:
    vocales = 0
    consonantes = 0
    for letra in ms.read():
        if letra.lower() in "aeiouáéíóú":
            vocales += 1
        else:
            consonantes += 1
    print(f"La cantidad de consonantes es {consonantes}")
    print(f"La cantidad de vocales es {vocales}")

    ms.seek(0)  

    archivo = ms.read().split()
    repetidas = Counter(archivo).most_common(50)

    print(f"Las palabras que más se repiten son: {repetidas}")
```
