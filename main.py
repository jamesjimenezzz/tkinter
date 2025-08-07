
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} barks and his breed is {self.breed}")
    


cyber = Dog("cyber", "corgi")


cyber.speak()