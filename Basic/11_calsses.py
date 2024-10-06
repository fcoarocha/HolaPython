### Classes ###

class MyEmptyPerson:
    pass


print(MyEmptyPerson())
print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname, alias = "sin alias"):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"
        self.alias = alias
    def walk(self):
        print(f"{self.full_name} esta caminando.")

my_person = Person("Francisco","Arocha")

print(f"{my_person.name} {my_person.surname}")

print(my_person.full_name)

print(my_person.alias)

my_person.walk()
      
