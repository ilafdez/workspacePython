frase="Aprendiendo a programar en python"
print(frase[0])
print(frase[1])
print(frase[-1])
print(frase[-2])

mi_substring1 = frase[:5]
print(mi_substring1)
mi_substring2 = frase[4:]
print(mi_substring2)

print(len(frase))
print(frase.upper())
print(frase.lower())
print(frase.title())

print(frase.count("pr"))#2
print(frase.count("pr", 0 ,6))#1
print(frase.find("pr"))#posicion de la primera vez que aparece
print("pr" in frase)
print("calc" in frase)
frase=frase.replace("python","python3")
print(frase)
print(frase.isnumeric())