#Funciones
def saludo(nombre):
    print(f"Hola, {nombre}. !Bienvenido¡")
    
saludo("Inés")

def saludo(nombre="Anónimo"):
    print(f"Hola, {nombre}. !Bienvenido¡")
    
saludo("Inés")
saludo()

#Parámetros posicionales vs. parámetros con palabras clave (keyword arguments)
def suma(a,b):
    res=a+b
    print(res)
    
suma(1,4)
suma(a=1,b=6)

def suma(*args):#pasas una lista de valores o una tupla
    res=0
    for value in args:
        res+=value
    print(res)
suma(1,6)

def suma(**kwargs):#pasas un diccionario
    res=0
    for value in kwargs.values():
        res+=value
    print(res)
suma(a=1,b=6)