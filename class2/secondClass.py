# String in python 
# We Use single cote , double cote and tripple cote for Creating String

str1 = 'Ammi Shah'
str2 = "My Name is Amir Shah"
str3 = """I am a full Stack Developer"""

# Escape Sequence Character
# \n , \t 

string = "This is a String.\nWe are Creating in python" #\n is used for to show Text in Next line
print(string)
tabbedString = "This is a String.\tWe are Creating in python " 
print(tabbedString) 

# inputString = input("Enter something for Print ")

# print(inputString)
# print(len(inputString))

# type Casting in python 

x = int(1)
y = float(2.8)
z = str(3)
print(x, y, z)

b = "Hello World"

# Slicing in String

print(b[2:5]) # it will print llo
print(b[:5]) # it will print Hello
print(b[6:]) # it will print World



print("String Conver to Uppercase: ",b.upper()) 

print("String convert to lowerCase using lower(): ",b.lower())


# The strip() method removes any whitespace from the beginning or the end:
a = "  Hello,World!  "
print(a.strip()) 

# String Concatenation using + operator
b = "Hello,"
c = "World!"
d = b + c
print(d)

# F-Strings
price = 59
txt = f"The Price is {price} rupees"
print(txt)

age = 26
txt2 = f"My name is Amir Shah and I am {age} years old"
print(txt2)


# slicing example 2
name = "Amir Shah"
print(name[0:4])

print(name[:4])
print(name[5:10])
print(name[5:])  # it will print from 5 to end of the string