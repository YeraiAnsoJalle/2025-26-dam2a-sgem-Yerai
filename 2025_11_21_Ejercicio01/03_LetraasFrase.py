def pedir_frase_sin_numeros(prompt="Ingresa una frase sin números: "):
    while True:
        texto = input(prompt)
        if any(ch.isdigit() for ch in texto):
            print("La frase contiene números. Intenta de nuevo.")
            continue
        return texto.strip()

frase = pedir_frase_sin_numeros()
palabras = frase.split()  # separa por espacios
palabras_ordenadas = sorted(palabras, key=lambda w: w.lower())
print("Palabras ordenadas:", palabras_ordenadas)