# Welcome to Python!

"""
We can use a multi line string literal
as a multi line comment
"""

# function coolFunction(){

# }

x = 5

if x > 2:
    print("it's a big x")
elif x < 2:
    print("it's a small x")
else:
    print("It's two")

#variables
#used to store data in a way we can reference by it's name
snake_case = "all lowercase separated by underscores"

GLOBAL_VAR = "typically all caps"
MyClass = "pascal case"
#Datatypes


#primitive

#numbers
my_integer = 8
my_float = 8.5

#strings
my_string = "A collection of characters 🍕"
# print(my_string + my_integer) THIS WILL THROW TYPE ERROR
# print(my_string + str(my_integer))
#str() int() float()

my_f_string = f"the string was {my_string} the number was {my_integer} "
# print(my_f_string)



#boolean -- True of False
my_bool = True



#composite

#list -- (similar to array in js)
#tuples -- like a list, but immutable (cannot change after declaration)
num_list = [1,2,3,4,5,6,7,8]
#   indexes 0 1 2 3 4 5 6 7
#access
four = num_list[3]
#reassignment
num_list[6] = 5
# print(num_list)
# print(four)

#functions used with list
my_list_length = len(num_list)
print("my length is:", my_list_length)
#min() max()

#methods used with list
#.pop() without argument will remove last element
#optionally -- it can take the index to remove

num_list.pop()
# print(num_list)
num_list.pop(1)
# print(num_list)

#.remove(element_to_remove)
num_list.remove(5)

#.append(element_to_add)
num_list.append("I'm new here")
print(num_list)





#dictionaries -- (similar to js objects)
# organized by KEY VALUE PAIR, in python keys are strings
# there are no indices in a dictionary

dict = {
    'key': 'value',
    'name': 'Spencer',
    'age': 35
}

print(dict["key"])

dict["making_this_up_now"] = "Some new value"
dict['age'] += 1

# test_number = 9
# test_number++ no ++ incrementer in py

# stored_value =dict.pop('key')
del dict['age']
# dict.clear()
print(dict)
# print(stored_value)
if 'age' in dict:
    x = 4
    x *= 9
    print(dict['age'])
else:
    print('No age found')


"""
Py        Js
==        ===
None      Null
not       !
or        ||
and       &&
is <-- is is used to check if both operands are the same object

"""







