# # String in python 
# # We Use single cote , double cote and tripple cote for Creating String

# str1 = 'Ammi Shah'
# str2 = "My Name is Amir Shah"
# str3 = """I am a full Stack Developer"""

# # Escape Sequence Character
# # \n , \t 

# string = "This is a String.\nWe are Creating in python" #\n is used for to show Text in Next line
# print(string)
# tabbedString = "This is a String.\tWe are Creating in python " 
# print(tabbedString) 

# # inputString = input("Enter something for Print ")

# # print(inputString)
# # print(len(inputString))

# # type Casting in python 

# x = int(1)
# y = float(2.8)
# z = str(3)
# print(x, y, z)

# b = "Hello World"

# # Slicing in String

# print(b[2:5]) # it will print llo
# print(b[:5]) # it will print Hello
# print(b[6:]) # it will print World



# print("String Conver to Uppercase: ",b.upper()) 

# print("String convert to lowerCase using lower(): ",b.lower())


# # The strip() method removes any whitespace from the beginning or the end:
# a = "  Hello,World!  "
# print(a.strip()) 

# # String Concatenation using + operator
# b = "Hello,"
# c = "World!"
# d = b + c
# print(d)

# # F-Strings
# price = 59
# txt = f"The Price is {price} rupees"
# print(txt)

# age = 26
# txt2 = f"My name is Amir Shah and I am {age} years old"
# print(txt2)


# # slicing example 2
# name = "Amir Shah"
# print(name[0:4])

# print(name[:4])
# print(name[5:10])
# print(name[5:])  # it will print from 5 to end of the string

# # Negative Indexing in String 
# fruitName = "Mango"
# print(fruitName[-5:-1])

# schoolName = "Government High School"
# print(schoolName.endswith("ool")) #Return True
# print(schoolName.endswith("School")) #Return True
# print(schoolName.endswith("sch")) #Return False

# # String functions in python
# print(schoolName.count("o")) # it will count the number of o in the string
# print(schoolName.count("h")) # it will count the number of h in the string
# print(len(schoolName)) 

# print(schoolName.capitalize()) # it will capitalize the first letter of the string

# print(schoolName.find("High")) 
# print(schoolName.find("i")) 

# print(schoolName.replace("High", "primary"))

# print(schoolName.upper())
# print(schoolName.lower())
# print(schoolName.count("o"))

# firstName = input("Enter your first name: ")
# print("Your Name length is: ", len(firstName))

# # Q1. Take a user's name as input and print its length.

# userName = input("Enter Your Name ")
# print("The length of User Name is: ", len(userName))

# # Q2. Take a sentence input and capitalize the first letter.

# inputSentence = input("Enter a Sentence ")
# print(inputSentence.capitalize())


# # Q3.Replace all spaces in a sentence with _.
# lang = "I Love python"
# print(lang.replace(' ', '_'))

# # Q4.Take a sentence and find the index of the word "python".
# sentence = "I am learning python programming"

# print(sentence.find("python"))

# # Q5.Convert a string into uppercase.
# text = "hasnain khan "

# print(text.upper())

# # Q6. Convert a string into lowercase.
# print(text.lower())

# # Q7. Count how many times "is" appears in a sentence.
# countWord ="This is a string and this is easy"
# print(countWord.count("is"))


# # Q8.Take a string and:

# # print length
# # convert to uppercase
# # count letter "a"
# takeString = input("Enter a String: ")
# print(len(takeString))
# print(takeString.upper())
# print(takeString.count("a"))

# Q9.Check whether a word exists in a sentence using find().
# isWordExist = 'Hello I am learning python for Agentic AI'

# print(isWordExist.find("python"))
# print(isWordExist.find("amir")) #this word is not exist it give output -1 

# # Q10.Take a sentence and replace "bad" with "good".
# sentence = "This is a bad day"
# print(sentence.replace("bad", "good"))

# 11.

# # Take a number and check:positive, negative, zero (using if elif else)

# num1 = 20

# if num1 > 0 :
#     print("Positive Number ")
# elif num1 < 0:
#     print("Negative number")
# else:
#     print("Zero")

# # Q12. Check whether a number is even or odd.

# checkNumber = 20

# if checkNumber % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# # Q13. Take marks input and print grade:(90+ → A, 80+ → B , 70+ → C ,below 70 → Fail

# marks = int(input("Enter your Marks "))

# if marks >= 90 and marks < 100:
#     print('A')
# elif marks >= 80 and marks < 90 :
#     print("B")
# elif marks >= 70 and marks < 80:
#     print("C")
# elif marks >= 0 and marks < 70:
#     print("Fail")
# else:
#     print("Please Enter Valid Marks between 0 to 100")


# # Q14.Take age input and check:(child,teenager , adult)

# age = int(input("Enter Your Age "))

# if age >= 0 and age < 13:
#     print("Child")
# elif age >= 13 and age < 20:
#     print("Teenager")
# elif age >= 20 and age < 60:
#     print("Adult")
# elif age >= 60:
#     print("Senior Citizen")
# else:
#     print("Please Enter Valid Age")

# # Q.15.Take two numbers and print the greater number.

# a = 20
# b = 30

# if a > b:
#     print(a, " is greater than b", b)
# elif a < b:
#     print(a, " is less than ", b)
# else:
#     print(a, " is equal to ", b)


# # Q.16.Check if a person is eligible for voting (18+).

# votingAge = int(input("Enter Your Age "))

# if votingAge >= 18:
#     print("You are eligible for voting")
# else:
#     print("You are not eligible for voting")


# Q.17.Take a password input:
# if length < 8 → Weak password
# otherwise → Strong password

passInput = input("Enter Your Password: ")

if len(passInput) < 8:
    print("Weak Password")
else:
    print("Strong Password")


# 18.Take a sentence:if "python" exists → print "Python found"
# else → print "Python not found"

takeSentence = input("Enter Sentence: ")
isExist = takeSentence.find("python")

if isExist != -1:
    print("Python found")
else:
    print("Python not found")
    