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
    def __init__(self,data):
        self.name = data['name']
        self.age = data['age']
        self.color = data['color']
        self.tricks = ['stay', 'sit', 'rollover']

    def bark(self):
        print(f'{self.name} lets out a bark!')
        return self, "also returning"
    
    def birthday(self):
        self.age += 1
        print(f'{self.name} has gotten older! They are now {self.age}')
        return
    
    def __repr__(self):
        str = f'{self.name} is a Dog Object Age: {self.age}  Color: {self.color} Tricks: '
        for trick in self.tricks:
            str += trick + " "
        return str

if Dog.is_cute:
    print('oh yeah, adorable')

dog_1 = Dog(dog_data_1)
dog_2 = Dog(dog_data_2)
# dog_1.new_att = "look what I just did"
# print(dog_1.name, dog_1.age, dog_1.color)
# print(dog_2.name, dog_2.age, dog_2.color)
print(dog_1)
# dog_1.birthday()
# x = dog_2.bark()[0].bark()
# print(x)
# dog_1.birthday()


