try:
    divisor=int(input("Introduce un divisor: "))
    dividendo=150
    resultado= dividendo/divisor
    print(resultado)
except ValueError:
    print("Número no válido")
except ZeroDivisionError:
    print("No se puede dividir entre 0")
finally:
    print("Ejecutar finally antes de salir")
    
