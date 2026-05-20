# student = ['amir shah', 'hasnain khan','anfal','Savid khan','Daud Shah', 'Shahzaib khan']

# print(student)
# print(student[0])
# print(student[1])
# print(student[2])
# print(student[3])
# print(student[4])
# print(student[5], "\n")


# student.append('Hassan Khan')
# for i in student:
#     print(i)

# list = [20, 10, 3, 7,12, 5]
# list.sort()   #sort the list in ascending order
# print(list)
# list.reverse()  #to reverse the list
# print(list)

# list.sort(reverse = True) #to sort the list in descending order
# print(list)

# list.insert(0, 30)  #insert element at the mention index
# print(list)

# list.insert(1, 200) #it insert the element at the first index
# print(list)

# print("The length of the list is:", len(list)) #to find the length of the list



# # 1.Create a list of 5 numbers and print it.
# numberList = [20,30,10,4,5]
# print(numberList)

# # 2.Add a new number to the list using append().
# numberList.append(6)
# print(numberList)

# # 3.Create a list of student names and print its length using len().
# studentNames = ['Ali Shah', 'Khan shah', "zohaib", "Rahat ", "obaid shah"]
# print(len(studentNames))


# # 4.Take 5 numbers from the user and store them in a list.
# userNumber = []
# for i in range(5):
#     num = int(input("Enter number "))
#     userNumber.append(num)
# print(userNumber)

# # 5.Print the first and last element of a list.
# print("First element: ", userNumber[0])
# print("Last element: ", userNumber[-1])


# 1. Create an empty list and add 5 fruits using append().
emptyList = []
emptyList.append("Banana")
emptyList.append("apple")
emptyList.append("peach")
emptyList.append("pineapple")
emptyList.append("Watermelon")
print(emptyList)

# 2. Add your favorite programming language to a list.
emptyList.append("Javascript")

# 3. Take 3 names from the user and append them to a list.
nameList = []
for i in range(3):
    name = input("Enter your name: ")
    nameList.append(name)
print(nameList)


# sort() Practice
# Create a list of numbers and sort them in ascending order.
numbers = [10,20,4,5,8]
print("Before Sorting:",numbers)
numbers.sort()
print("After Sorting:",numbers)

# Sort a list of names alphabetically.
# Take marks of students in a list and sort them.