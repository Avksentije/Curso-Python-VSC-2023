#Hola mundo.
print("Hola, Python")
print("Soy Tania")

#Consultar tipo de dato.
print(type("Hola, mundo!")) #Tipo 'str'
print(type(5)) #Tipo 'int'
print(type(5.5)) #Tipo 'float'
print(type(True)) #Tipo 'boolean'
print(type(3 + 1j)) #Numeros complejos 'complex'
print(type([1, 2, 3])) #Tipo 'lista'

#Operadores.
print(2 + 5) #Adicion
print(2 - 5) #Sustraccion
print(2 * 5) #Producto o multiplicacion
print(2 / 5) #Division
print(2 ** 5) #Exponencial
print (2 % 5) #Modulo
print(2 // 5) #Floor division operator


#Comienzo a definir variables.
x = 1    # int
y = 2.8  # float
z = 1j   # complex
w = -87.7e100 #float
print(w)
a = 12E4 #float
print(a)

print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(a))

print("Hola " + "Python") #Concatenación.
print("Hola " + str(5)) #Se concatenan mismo tipo de datos.
print("Hola " * 2)
my_float = 2.8 * 2
print("Hola " * int(my_float))


#Aplicaciones en bioinformática DNA, usando variable tipo str.
b = "Hello, World!"
print(b)
print(type(b))
print(b[2:5]) #Inicia en 0, y el 5 no se incluye.
print(b[:5])
print(b[-5:-2]) #Use negative indexes to start the slice from the end of the string.
print(b.upper()) #método upper
print(b.lower()) #método lower

b = "    Hello, World!  " #Reconoce los espacios antes y después.
print(b[2:5]) #Inicia en 0, y el 5 no se incluye.
print(b[:5])
print(b[-5:-2]) #Use negative indexes to start the slice from the end of the string.
print(b.upper())
print(b.lower())

#Acá me imagino sustituyendo T por U, o encontrando CpG
m = "   Hello, beautiful World!      "
print(m.strip())  #método strip, elimin espacios antes y después de la frase.
print(m.replace("H", "J"))  #método replace
print(m.split(",")) #se puede "afinar" un split desde strip :))
x = m.strip()
z = print(x.split(","))


#Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)



