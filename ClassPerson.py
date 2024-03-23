#creating a class Person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"My name is {self.name}, I am {self.age}, and I am {self.gender}.")


person1 = Person("Hambugger", 67, "Female")
person1.introduce()
