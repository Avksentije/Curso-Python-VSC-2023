#Clases

class MyEmptyPerson:
    pass #palabra clave para evitar errores por falta de código.

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person("Tania", "RC")
print(my_person.name)
print(my_person.surname)


class Person_dos: #definición de objetos
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} e stá caminando")

my_person = Person_dos("Tania", "RC")
print(my_person.full_name)
my_person.walk()









