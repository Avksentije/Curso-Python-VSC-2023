#Excepciones

numberOne = 5
numberTwo = 1
numberTwo = "1"

try: 
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")