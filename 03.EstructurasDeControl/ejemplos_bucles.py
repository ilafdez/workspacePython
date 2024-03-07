#while
contador=0
while(contador<5):
    contador+=1
    print("Iteración número",contador)
    
print("FIN")
    
contador=0
while (contador<5):
    contador+=1
    print("Iteración número {}".format(contador))
    if contador==3:
        break
    
print("FIN")

#FOR (FOREACH)
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
for alumno in alumnos:
    print(alumno)
    
#recorrer un string
alumno="Gaizka"
for letra in alumno:
    print(letra)
    
numeros=[5,46,3,5,2,5,55,9]
for numero in numeros:
    if numero % 2==0:
        continue
    print(numero) 

#For con else - Si termina el for completo
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
for alumno in alumnos:
    print(alumno)
else:
    print("No quedan más alumnos")

#función range() - Para hacer un bucle iterativo
for i in range(3):
    print(i)
    
for i in range(1,10,2):
    print(i)
    
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
for i in range(len(alumnos)):
    print(alumnos[i])

