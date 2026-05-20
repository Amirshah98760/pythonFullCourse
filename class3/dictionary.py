#Dictionary in python is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure. 

student ={
    "stdname": "Amir shah",
    "age": 20,
    "course": "Python",
    "grade": "A"
}
print(student, "\n")

print(student["stdname"])
print(student["age"])
print(student["course"])
print(student["grade"])

changeAge = student["age"] = 26
print(student, "\n")

#Print Dictionary using loop

for key in student:
    print(key , ":", student[key])


print(student.keys()) # Return Only keys
print(student.values()) #Return Only Values

print(student.items()) #Return key-value pairs as a list of tuples

car ={
    "brand":"Toyota",
    "model":"Corola",
    "Year":2024,
    "color":"black"
}

print(car["brand"])
print(car["model"])
print(car["Year"])
print(car["color"], "\n")

for i in car:
    print(i , ":", car[i]);


# Practice Questions
# Create a dictionary of a student.

studentData = {
    "name":"Amir shah",
    "rollN0":439,
    "age": 25,
    "section":"G",
    "university":"University of Agriculture Peshawar"
}
# Print all keys.
print(studentData.keys())

# Print all values.
print(studentData.values())

# Update age in dictionary.
studentData["age"] = 26

# Add a new key "city".
studentData["city"]= "Peshawar"
print(studentData)
# Remove a key using pop().
studentData.pop("city")
print(studentData, "\n")

# Loop through a dictionary.
for key in studentData:
    print(key , ":", studentData[key])

# Create a nested dictionary.
students ={
    "student1":{
        "name":"Amir shah",
        "rollN0":439,
        "age": 25,
        "section":"G",
        "university":"University of Agriculture Peshawar"
    },
    "student2":{
        "name":"Ali shah",
        "rollN0":440,
        "age": 24,
        "section":"G",
        "university":"University of Agriculture Peshawar"
    }
}



# Take user input and store in dictionary.

userInput = {}
name = input("Enter your name: ")
userInput["name"] = name
print(userInput)

personalInfo = {
    "name":"Amir shah",
    "age":26,
    "city":"Peshawar",
    "course":"Python"
}

print(personalInfo["city"])

personalInfo["email"] = "amirshah12@gmail.com"

print(personalInfo)
personalInfo["age"] = 25

print("The length of dictionary is : ",len(personalInfo))

# print(personalInfo.clear())

# Count how many keys exist in a dictionary.
print(len(personalInfo))

mobileInfo ={
    "brand":"Samsung",
    "model":"Galaxy S21",
    "storage":"128GB",
    "price": 150000
}
print(mobileInfo["brand"])
print(mobileInfo["model"])
print(mobileInfo["storage"])
print(mobileInfo["price"])

print(type(mobileInfo))