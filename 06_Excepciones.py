#Excepciones

numberOne = 5
numberTwo = 1
numberTwo = "2"

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    #Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")
finally: #Opcional
    #Se ejecuta siempre
    print("La ejecución continúa")



#Excepciones por tipo de dato

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un error")


try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un error de tipo ValueError")
except TypeError:
    print("Se ha producido un error de tipo TypeError")
