#Tuple 

numbers = (95,30,60,20,150)
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4] , "\n")

for i in numbers:
    print(i)
print(type(numbers))

thistuple = ("apple", "banana", "cherry", "pineapple", "kiwi", "melon", "mango")
print(thistuple)

for i in thistuple:
    print(thistuple.index(i), i)

myNumbers = (20, 30, 10, 4, 20, 5)
# myNumbers.insert(0, 100) #tuples are immutable, so we cannot change the values of a tuple
print(myNumbers)

# myNumbers[0]= 100 #we cannot change the values of a tuple
print(len(myNumbers)) #to find the length of a tuple
print(type(myNumbers)) 

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1.count(40)) #to count the number of times a value appears in a tuple
print(tuple1.index("abc")) #to find the index of a value in a tuple


string = "Hello"
print(string[0])
print(string)
print(string.replace("Hello", "Hi"))
