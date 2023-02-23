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