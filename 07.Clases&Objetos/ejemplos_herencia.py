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

class Estudiante(Persona):#existe la multiherencia y separado por coma
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.nota_media = 0
        self.repetidor = False
    def es_repetidor(self):
        print(self.repetidor)
           
p2= Estudiante("Josean", "Hernández", 40)
p2.es_repetidor()
