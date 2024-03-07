#res ambito local, dentro de la función, y cuando se termina la ejecución no está en memoria
def suma(a,b):
    res=a+b
    print(res)
print(res)#Error
suma(1,4)
suma(a=1,b=6)

#ámbito global
a=5
def multiplica_por_dos():
    print(a*2)
multiplica_por_dos()

x = 10 
def mostrarX():
    x = x + 2 #Error, podemos acceder pero no modificar
    print("El valor de x es", x)
mostrarX()

x = 10 

def mostrarX():
    global x
    x = x + 2
    print("El valor de x es", x)  
mostrarX()
