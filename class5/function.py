def myFunction():
    print("Hello from a function")


myFunction()  # Calling the function to execute the code inside the function
myFunction() 
myFunction() 

print("The function has been called three times.")

def greet():
    print("Hello, Welcome to the function tutorial!")

greet()

# function with parameters 
def greet(name):
    print("Hello , ", name)

greet("Amir shah")

def add(a, b):
    return a + b

result = add(20, 30)
print("a + b = ",result)

# pass default value to parameters 

def greet(name = "guest"):
    print(name)

greet()
greet("Suhaib khan")

# Multiple Return Values
def calc(a, b ):
    return a + b, a * b

res = calc(20,10)
print(res)

# lambda function are anonymous function which is defined without a name and it can take any number of arguments but can only have one expression.

square = lambda x: x * x
print(square(10))

add = lambda x, y: x + y
print(add(20, 30))

numbers = [1, 2, 3, 4, 5]
square_numbers = list(map(lambda x: x * x, numbers))
print(square_numbers)

nums = [2, 4, 5, 6, 7]
square_nums = list(map(lambda x : x *  x, nums))

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# use map and filter in normal function

def square(x):

    return x * x

number = [1,2,3,4]
square_nums = list(map(square, number))
print(square_nums)

