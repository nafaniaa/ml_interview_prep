class Dog():
    # Простая модель собаки

    def __init__(self, name, age):
        # инициализирую атрибуты name и age
        self.name = name
        self.age = age 
    
    def sit(self):
        print(f"{self.name} is sitting now!")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Sunshine', 2)



print(f"My dog's name is {my_dog.name}")
print(f"It is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()


name = input("And what is your dog's name?\n")
age = input("And how old is it?\n")

your_dog = Dog(name, age)

print(f"Oh, {your_dog.name} is very cute!")
