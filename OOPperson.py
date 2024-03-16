class Person:
    name = "Hambugger"
    age = 95
    gender = "Female"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    
    def introduce(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I am {self.gender}.")
        

person1 = Person("Hambugger", 95, "Female")

person1.introduce()
