class Animal():  
    def speak(self):
        return "Sound"
    

class Cat(Animal):
    def speak(self):
        return "Meow"
    
cat = Cat()
print(cat.speak())