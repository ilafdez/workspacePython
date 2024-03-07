class Persona:
    nombre="Josune"
    edad=24
    
    def camina(self):
        print(self.nombre + " está caminando" )

p1=Persona()
p1.camina()
print(p1.nombre)

#Constructor __init__ (sólo puede existir uno)
class Persona:
    #Atributos de clase o estático
    contador=0
    def __init__(self, nombre, apellido, edad):#self hay que pasarlo
        #Atributos de instancia
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        Persona.contador+=1
        
    def camina(self):
        print(self.nombre + " está caminando" )
        
p2= Persona("Josean", "Hernández", 40)
p2.camina()
print(p2.contador)
p3=Persona("Alex", "Fernández", 10)
print(Persona.contador)

#Protected y private
class Persona:
    def __init__(self, nombre, apellido, edad):#self hay que pasarlo
        #Atributos de instancia
        self.__nombre=nombre
        self._apellido=apellido
        self._edad=edad
        
    def camina(self):
        print(self.nombre + " está caminando" )

p4=Persona("Aiur", "González", 12)
print(p4._apellido)
print(p4.__nombre)
