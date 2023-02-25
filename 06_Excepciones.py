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


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as yo_defino_el_nombre_de_esta_variable_que_almacena_el_tipo_de_error:
    print(yo_defino_el_nombre_de_esta_variable_que_almacena_el_tipo_de_error)
except Exception as esta_otra_de_aca_también:
    print(esta_otra_de_aca_también)

#pero también lo puedo escribir así, para que sea más estándar jaja
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)