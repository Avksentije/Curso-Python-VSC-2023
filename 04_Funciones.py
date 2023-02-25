#Funciones

#Centraliza código, recursividad; es el concepto central de la programación orientada a objetos.

#Usamos la palabra reservada "def" en la sintaxis de crear una función.

def my_function():
    print("Esto es una función")

my_function() #llamo a la función que definí previamente


def sum_two_values(first_number, second_number): #dentro del paréntesis coloco dos parámetros
    print(first_number + second_number)

sum_two_values(5, 7) #suma enteros
sum_two_values("5", "7") #concatena cadenas de texto
sum_two_values(54754, 71231)
sum_two_values(1.6, 1.25) 

#Concluyo la importancia de definir el tipo de dato con el que se alimenta un programa. 
#Esto me remite a SQL

def sum_and_return (first, second):
    return first + second

my_result = sum_and_return(10, 5)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}") #formateamos
print_name("Tania", "RC")


def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")
print_name_with_default("Tania", "RC", "Amurita")

def print_infinite_texts(*text): #usando * puedo generar infinito, parámetros separados por coma
    print(text)
print_infinite_texts("Hola", "textos", "infinitos", "puedo", "agregar", "los que quiera")
print_infinite_texts("o poquitos") #estas opciones nos funcionan para los "For" que están ligados a una BD


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)