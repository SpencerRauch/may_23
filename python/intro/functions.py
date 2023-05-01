#functions -- blocks of reusable code -- may take in arguments -- will return something (even if it's nothing)

def say_hello(name="Default", times=3):
    for i in range(times):
        print(f"Hello, {name}")
    return f"Hello {name}" * times


hello_message = say_hello('bob', 9)
print(hello_message)

second_message = say_hello(times=10)
print(second_message)

print(10 % 3)

#print vs return -- 

#print is just like console.log in that it's meant to display something to the developer
# just a display to a terminal/console/cli

#return -- Passes info back from the called function to its caller (-Allen)
# A FUNCTION CALL IS REPLACED BY ITS RETURN

#default parameters 
#when you supply a default value to use if a parameter is not passed an argument
#note that parameters fill up left to right by default
#defaulted parameters must come at the end of your parameter

#named arguments
#when you specify which parameter the argument is for
#named arguments must come after positional arguments
