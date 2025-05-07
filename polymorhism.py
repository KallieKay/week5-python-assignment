class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
class Cow:
    def speak(self):
        return "Moo!"
    
for animal in [Dog(), Cat(), Cow()]:
    print(animal.speak())

    class Jaguar:
        def move(self):
            return "Sprinting"
        
    class Kangaroo:
        def move(self):
            return "Hopping"
        
    for wild_animal in [Jaguar(), Kangaroo()]:
        print(wild_animal.move())