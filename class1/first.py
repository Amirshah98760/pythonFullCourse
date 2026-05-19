print("Hello, World!")
print("Welcome to Python programming.")
print("My name is Amir shah")
print("I am learning Python.")


# a = 20
# b=30


# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

a= 10
b= 20
name = '''My name is Amir shah
I am learning Python.'''


print(name)
#one line comment 
"""
This is a multi-line comment
or documentation string.
"""

print("The sum of a and b is:", a + b,
      "\nThe difference of a and b is:", a - b,
      "\nThe product of a and b is:", a * b,
      "\nThe quotient of a and b is:", a / b);

developer_name = "Amir shah"
learning_language = "Python"
print("My name is", developer_name, "and I am learning", learning_language);

num1 = 20 #integer 

num2 = 3.14 #float

myName = "Amir shah" #string
isLearning = True #boolean
print("The value of num1 is:", num1)
print("The value of num2 is:", num2)
print("The value of myName is:", myName)
print("The value of isLearning is:", isLearning)

print("The type of num1 is:", type(num1))
print("The type of num2 is :", type(num2))
print("The type of myName is:", type(myName))
print("The type of isLearning is:", type(isLearning))


name = "Amir shah"
age = 25
height = 5.8
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Write a program to swap two numbers.
num3 = 10
num4 = 20
print("Before swapping: num3 =", num3, "num4 =", num4)
# Swapping
temp = num3
num3 = num4
num4 = temp
print("After Swapping:  num3 = ", num3,"num4 = ", num4 )

enterName = input("Enter your Name ")
print("Welcome ", enterName)

str = input("Enter a string: ")
print(len(str));

# Write a program to join two strings.
str1 = "Hello"
str2 = "World"

# Joining the strings
joined_str = str1 + " " + str2
print("Joined String:", joined_str)

# Count how many characters are in your name.
name = input("Enter your name: ")
name_length = len(name)
print("The number of characters in your name is:", name_length)

findChar = 'Hasnain Khan'
charLength = len(findChar)
print(charLength)

userInput1 = int(input("Enter  num1 "))
userInput2 = int(input("Enter num2 "))

averageofTwoNumbers = (userInput1 + userInput2) / 2

print("The average of two numbers is:", averageofTwoNumbers)

length = 20
width = 10

area = length * width
print("The area of the rectangle is:", area)

circle_radius = 5
pi = 3.14
circle_area = pi * (circle_radius ** 2)
print("The area of the circle is:", circle_area)

# Write a program that checks:
# Is a number greater than 100?
# Is a number even?

number = int(input("Enter a Number "))

if number > 100:
    print("Number you enter is Greater than 100 ")
if number % 2 == 0:
    print("The number is Even")

isAdmin = True
isActive = False

print(isAdmin and isActive)
print(isAdmin or isActive)
# print(isAdmin not isActive)

# Make a student info program that stores:
# name
# class
# marks
# percentage

# Then print all information neatly.

student_name = input("Enter Student Name: ")
student_class = input("Enter Student Class: ")
student_marks = float(input("Enter Student Marks: "))
total_marks = 100
student_percentage = (student_marks / total_marks) * 100
print("\nStudent Information:")
print("Name:", student_name)    
print("Class:", student_class)
print("Marks:", student_marks)
print("Percentage:", student_percentage, "%")


val1 = 30
val2 = 20

if val1 > val2:
    print("Val1 is greater than val2")
elif val2 > val1:
    print("val2 is greater than val1")
else:
    print('Val1 and Val2 are equal')