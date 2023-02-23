#Loops >

#While true

my_condition = 0

#while my_condition < 10: 
    #print(my_condition)
    #my_condition += 2
#if my_condition == 10: #si ponemos un if, aqui ya estamos fuera del while, cuidado
   #print("Mi condicion es igual a 10")
#else:
    #print("Mi condicion es mayor o igual que 10")

#print("La ejecucion continua")


#while my_condition < 20: 
    #print(my_condition)
    #my_condition += 1
    #if my_condition == 10:
        #print("Mi condicion es igual a 10")
#else:
    #print(my_condition)


while my_condition < 20: 
    print(my_condition)
    my_condition += 2
    if my_condition == 10:
        print("Se detiene la ejecución")
        break
else:
    print(my_condition)


#For: la función for está ligada a un conjunto de valores


my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)


tania = ["plantas", "pintura", "agricultura"] #lista
amurita = ("filosofia", "musica", "pensamiento") #tupla
playlist_album = {"Agua", "Bonito", "Me gusta como eres"} #set
person_info = { #diccionario
   'firstname':'Amurita',
   'lastname':'Klozevits',
   'country':'Finland',
   'city':'Helsinki',
   'age':35,
   'is_married': False
   }

for element in tania:
    print(element)

for element in amurita:
    print(element)

for element in playlist_album:
    print(element)

for element in person_info: # en un diccionario, imprime solo los campos que integran al diccionario
    print(element)

for element in list(person_info.values()): #al diccionario lo debemos transformar en lista y obtener los valores para que los muestre
    print(element) 


for element in person_info: # en un diccionario, imprime solo los campos que integran al diccionario
    print(element)
else: 
    print("El bucle ha finalizado")