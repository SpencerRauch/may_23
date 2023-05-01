#Loops -- code that repeats a set amount of times based on a condition

# for (let i = 0; i < 10; i++) <-- js
"""
for ____ in ____ :
    code to execute
"""

#first blank -- iterative variable


#second blank -- sequence or collection that we are iterating over

#iterating over a range:

#start -- optional, default of 0 -- the number we will start our sequence at INCLUSIVE
#stop -- required EXCLUSIVE -- the number we will end BEFORE
#step -- the amount that we will change per step (can be positive or negative)

# for i in range(5,100,2):
#     print(i)

# for i in range(50,-100,-10):
#     print(i)

# for i in range(2,101,2):
#     print(i)

string = "What is this going to do when we iterate?"
# when we iterate over a string, our iterative variable represents each character in turn

# for char in string:
#     print(char)

desserts = ['cake', 'cheesecake', 'ice cream', 'chocolate', 'pizookie']
# when we iterate over a list, our iterative variable represents each element in turn

for dessert in desserts:
    dessert = "Pie"
    # print(dessert)

# print(desserts)

for i in range(len(desserts)):
    desserts[i] = "Pie"
#to perform an assignment in the list, we need access to an index

# print(desserts)


pet_one = {
    'name': 'Teddy',
    'type': 'dog'
}

pet_two = {
    'name': 'Jax',
    'type': 'fish'
}

# for key in pet_one:
#     print(f"Key: {key} Value : {pet_one[key]}")

# for key, value in pet_one.items():
#     print(f"Key is {key} Value is {value}")

all_pets = [pet_one, pet_two]

all_pets[0]['name']

for one_pet in all_pets:
    for key in one_pet:
        print(f"Key: {key} Value : {one_pet[key]}")


#while
x = 5
while x > 0:
    print(x)
    x +=1
    #make sure your logic trends towards breaking the loop

