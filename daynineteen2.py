class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def show_info(self):
        return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}"

class Lion(Animal):
    def make_sound(self):
       return "roar"

class Elephant(Animal):
    def make_sound(self):
        return "blow"

class Panda(Animal):
    def make_sound(self):
        return "chew"
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def show_all_animals(self):
        for animal in self.animals:
            print(animal.show_info())


zoo = Zoo("City Zoo Redux")
lion = Lion("Alex", 5, 190)
elephant = Elephant("Dumbo", 10, 5400)
panda = Panda("Po", 4, 1540)

zoo.add_animal(lion)
zoo.add_animal(elephant)
zoo.add_animal(panda)

zoo.show_all_animals()

print("\n")
print("Lion "+lion.make_sound()+"s")
print("Elephant "+elephant.make_sound()+"s")
print("Panda "+panda.make_sound()+"s")