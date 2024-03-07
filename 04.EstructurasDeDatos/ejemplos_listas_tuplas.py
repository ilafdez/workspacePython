#Listas: más de un elemento de forma indexada
alumnos=["Gaizka", "Mikel", "Jon","Ruben"]
print(alumnos[0])
print(alumnos[len(alumnos)-1])
alumnos[1]="Asier"
print(alumnos[1])

alumnos.append("Manel")
print(alumnos)
alumnos.insert(0,"Markel")
print(alumnos)
alumnos.remove("Markel")
print(alumnos)
alumnos.pop()
print(alumnos)
alumno_eliminado=alumnos.pop(1)
print(alumnos)
print(alumnos.index("Gaizka"))
alumnos2= ["Jon Ander", "Andrea", "Michael"]
alumnos.extend(alumnos2)
print(alumnos)
alumnos.reverse()
print(alumnos)
sorted_alumnos= sorted(alumnos)
print(alumnos)
print(sorted_alumnos)

#Acceder a varios elementos
lista=[7,2,5,4,72,33]
print(lista[1:3])
print(lista[:3])
print(lista[2:])

#Recorrer una lista
for numero in lista:
    print(numero)
    
for i in range(len(lista)):
    print(lista[i])
    
#Tuplas - listas inmutables
valores=(1,4,2,5,13,0)
valores_mixtos=(1,4,2,5,"Trece",0)
print(valores_mixtos)
print(valores_mixtos[4:5])


