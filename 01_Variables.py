#Variables:


#Buenas practicas
#a) Al crear variables, usamos minusculas y guiones bajos. 
#b) Evitemos nombres largos.

my_string_variable = "Mi primer variable"
print(my_string_variable)
print(len(my_string_variable))

my_int_variable = 123
print(my_int_variable)

#Podemos transformar un tipo de variable int a str:
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

print('Hello', ',','world') #Imprimir diferentes argumentos.

# Concatenacion de variables en un print
print(my_string_variable,my_int_variable,my_bool_variable)

#When we assign a certain data type to a variable, it is called variable declaration. 
# For instance in the example below my first name is assigned to a variable first_name. 
# The equal sign is an assignment operator. Assigning means storing data in the variable.
# The equal sign in Python is not equality as in Mathematics.

first_name = 'Tania'
last_name = 'Avksentije'
country = 'Sweden'
city = 'Stockholm'
age = 33
is_married = False
skills = ['HTML', 'CSS', 'SQL', 'Python']

name, surname, alias, age = "Atenea", "Morita", "Princess", "4"
print("La perrita mas bonita es: ", name, surname,". Tiene ", age, "años. Y le gusta que le digan ", alias,".")

#Listas, tuplas, sets, diccionarios

#a) Lista: List items are ordered, changeable, and allow duplicate values.
tania = ["plantas", "pintura", "agricultura"]
print(tania[0])
print(tania[1])
print(tania[2])

nuevos_valores = ("misticismo", "arte digital")
tania_dos = tania.extend(nuevos_valores) #método agregar elementos
print(nuevos_valores)
print(tania)
print(len(tania))
print(type(tania))

print(tania.pop(3)) #eliminamos cualquier elemento de la lista usando pop
print(tania)


#b) Tupla: A tuple is a collection which is ordered and unchangeable.
amurita = ("filosofia", "musica", "pensamiento")
print(amurita[0])
print(amurita[1])
print(amurita[2])
print(len(amurita))
print(type(amurita))

#c) Sets: A set is a collection which is unordered, unchangeable*, and unindexed.
# *Aunque no se puede cambiar un valor, si pueden eliminarse o añadir nuevos valores.

playlist_album = {"Agua", "Bonito", "Me gusta como eres"}
print(playlist_album)

playlist_album.add("Grita")
print(playlist_album)

print(len(playlist_album))
print(type(playlist_album))

#d) Diccionario: Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

person_info = {
   'firstname':'Amurita',
   'lastname':'Klozevits',
   'country':'Finland',
   'city':'Helsinki',
   'age':35,
   'is_married': False
   }
print(len(person_info)) #se obtiene el número de elementos del diccionario.
print(person_info.get("country")) #método get, directamente. 

y = person_info["city"] #Definir una variable.
print(y)

x = person_info.get("city") #Consultar obteniendo un dato. 
print(x)


my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)


#Formateo

name, surname, age = "Tania", "Rodríguez", 33

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age)) #Este es el formato a elegir :) imprime el objeto
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, age)) #Usamos % cuando el caracter ya se encuentra formateado
print("Mi nombre es {name} {surname} y mi edad es %d" %(name, surname, age)) 
