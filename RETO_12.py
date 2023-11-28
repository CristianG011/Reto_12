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