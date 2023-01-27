class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age, type, owner):
        """Initialize name and age attributes."""    
        self.name = name  # attribute, properties
        self.age = age
        self.type = type
        self.owner = owner


    def sit(self):  # method, behavour
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

    def describe_pet(self,):
        return f"I have a {self.type}. \nMy {self.type} name is {self.name}. \nHis age is {self.age}."
    
    def my_name(self):
         print(f"my name is {self.owner}")


puppy = Dog('willi', 2, 'huskey', "jak")
pitbul = Dog('alex', 30, 'pitbul', 'sam')

again = Dog('jummy', 5, 'rotvilor', 'ali')

puppy.my_name()
# data = my_name("muhammad", 'ali', 'jinnah')

# print("Mujhe is linka ka code dekhna hai: ",data)
