#OOP

#Classes and Instances (Objects)

#What is a class? blueprint  -- it defines the methods and attributes we can expect from our Objects (Instances)
# classes create a custom data type

#object/instance -- the actual thing we create with a blueprint (class)

dog_data_1 = {
    'name': 'Fido',
    'age': 2,
    'color': 'brown'
}

dog_data_2 = {
    'name': 'Spot',
    'age': 4,
    'color': 'white with a brown spot'
}

#self is similar to "this" in javascript
#in a class, self refers to a single instance/object

#attributes describe our objects with values
#methods

class Dog:
    # def __init__(self, name_param, age, color):
    #     self.name = name_param
    #     self.age = age
    #     self.color = color
    is_cute = True
    all_dogs = []

    def __init__(self,data,roommate=None):
        self.name = data['name']
        self.age = data['age']
        self.color = data['color']
        self.tricks = ['stay', 'sit', 'rollover']
        self.roommate = roommate
        self.roommates = []
        Dog.all_dogs.append(self)


    def bark(self):
        print(f'{self.name} lets out a bark!')
        return self, "also returning"
    
    def birthday(self):
        self.age += 1
        print(f'{self.name} has gotten older! They are now {self.age}')
        return
    
    def greet_roommate(self):
        if self.roommate == None:
            print("The dog looks around and decides to just enjoy its freedom instead")
        else:    
            print(f'{self.name} walks up to {self.roommate.name}')
            self.roommate.say_hello()

    
    def __repr__(self):
        str = f'{self.name} is a Dog Object Age: {self.age}  Color: {self.color} Tricks: '
        for trick in self.tricks:
            str += trick + " "
        return str
    
    @classmethod
    def show_all_dogs(cls):
        for one_dog in cls.all_dogs:
            print(one_dog)

    @classmethod
    def bark_party(cls):
        print("The bark party starts!")
        for one_dog in cls.all_dogs:
            one_dog.bark()

    @staticmethod
    def calculate_dog_years(years):
        return years * 7
    
    @staticmethod
    def is_valid_dog(data):
        is_valid = True
        if 'name' not in data:
            is_valid = False
        return is_valid


class Human:
    def __init__(self,name):
        self.name = name

    def move_in_with_dog(self, dog):
        dog.roommates.append(self)

    def say_hello(self):
        print(f'{self.name} says hello!')

    def __repr__(self):
        return self.name


# if Dog.is_cute:
#     print('oh yeah, adorable')
# if Dog.is_valid_dog(dog_data_1):
#     dog_1 = Dog(dog_data_1)

# dog_2 = Dog(dog_data_2)
# me = Human('Spencer')

# dog_2.roommate = me


# dog_1.new_att = "look what I just did"
# print(dog_1.name, dog_1.age, dog_1.color)
# print(dog_2.name, dog_2.age, dog_2.color)
# print(dog_1)
# dog_1.birthday()
# x = dog_2.bark()[0].bark()
# print(x)
# dog_1.birthday()


#class methods 
"""
no access to any instance variables
operate on the class level only
no reference to self
call it from the class itself
can access class attributes
"""

#static methods
"""
unchanging -- doesn't mutate anything in the class
utility function that relates to class
often used to validate data coming into our class
"""

# Dog.show_all_dogs()
# Dog.bark_party()
me = Human('Spencer')
spot = Dog(dog_data_2,me)
free_dog = Dog(dog_data_1)

carlie = Human('Carlie')
allen = Human('Allen')

allen.move_in_with_dog(spot)
carlie.move_in_with_dog(spot)

# print(spot.roommate)
spot.greet_roommate()
free_dog.greet_roommate()

print(spot.roommates)
