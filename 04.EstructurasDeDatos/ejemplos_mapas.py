#Mapas o diccionarios
estudiante={
    "nombre": "Iñaki Perurena",
    "edad":30,
    "nota_media":7.25,
    "repetidor": False,
}
print(estudiante)
print(estudiante["edad"])
print(estudiante.get("edad"))
estudiante["suspensos"]=1
estudiante.update({"aprobados":5})
print(estudiante)
#Métodos de diccionarios
print(estudiante.keys())
print(estudiante.values())
print(estudiante.pop("aprobados"))
print(estudiante)
if "aprobados" in estudiante:
    print("Tiene aprobados")
else:
    print("No tiene aprobados")
    
if "Iñaki Perurena" in estudiante.values():
    print("Este es Iñaki")
else:
    print("Este no es Iñaki")
    
#Recorrer un mapa
for key in estudiante:
    print(key)

for key in estudiante:
    print(estudiante.get(key))
    
for value in estudiante.values():
    print(value)

for key,value in estudiante.items():
    print(f"El valor de {key} es {value}")

