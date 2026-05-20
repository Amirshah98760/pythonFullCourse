student = ['amir shah', 'hasnain khan','anfal','Savid khan','Daud Shah', 'Shahzaib khan']

print(student)
print(student[0])
print(student[1])
print(student[2])
print(student[3])
print(student[4])
print(student[5], "\n")


student.append('Hassan Khan')
for i in student:
    print(i)

list = [20, 10, 3, 7,12, 5]
list.sort()   #sort the list in ascending order
print(list)
list.reverse()  #to reverse the list
print(list)

list.sort(reverse = True) #to sort the list in descending order
print(list)

list.insert(0, 30)  #insert element at the mention index
print(list)

list.insert(1, 200) #it insert the element at the first index
print(list)

print("The length of the list is:", len(list)) #to find the length of the list



# 1.Create a list of 5 numbers and print it.
numberList = [20,30,10,4,5]
print(numberList)

# 2.Add a new number to the list using append().
numberList.append(6)
print(numberList)

# 3.Create a list of student names and print its length using len().
studentNames = ['Ali Shah', 'Khan shah', "zohaib", "Rahat ", "obaid shah"]
print(len(studentNames))


# 4.Take 5 numbers from the user and store them in a list.
userNumber = []
for i in range(5):
    num = int(input("Enter number "))
    userNumber.append(num)
print(userNumber)

# 5.Print the first and last element of a list.
print("First element: ", userNumber[0])
print("Last element: ", userNumber[-1])


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
# nameList = []
# for i in range(3):
#     name = input("Enter your name: ")
#     nameList.append(name)
# print(nameList)


# sort() Practice
# Create a list of numbers and sort them in ascending order.
numbers = [10,20,4,5,8]
print("Before Sorting:",numbers)
numbers.sort()
print("After Sorting:",numbers)

# Sort a list of names alphabetically.
list = ['c', 'b','a','d','g']
list.sort()
print("After Sorting (Ascending):",list)  

# Take marks of students in a list and sort them.
marks = [80, 90, 70, 85, 95]
print("Marks before sorting:", marks)
marks.sort()
print("Marks after sorting:", marks)


# sort(reverse=True) Practice
# Sort a list of numbers in descending order
numList = [20,10,300,10,30]
numList.sort(reverse=True)
print(numList)


# Find the highest number after sorting in reverse order.
highest = max(numList)
print(highest)



# Sort a list of prices from highest to lowest.
listofPrice = [300, 200, 100, 50, 40]
listofPrice.sort(reverse=True)
print(listofPrice)

# insert() Practice
# Insert a number at index 2.
number = [20,3,2,5,6,8]
number.insert(2,5)
print(number)

# Insert your name at the beginning of a list.
nameList = ['Ali', 'Khan', 'Shah']
nameList.insert(0, 'Amir Shah')
print(nameList)

# Add a new city name at index 1.
cityList = ['Karachi', 'Lahore', 'Islamabad']
cityList.insert(1, 'Peshawar')
print(cityList)

# remove() Practice
# Remove a specific number from a list.
numberList = [20, 10, 3, 7,12, 5]
numberList.remove(3)

# Remove "apple" from a fruit list.
emptyList.remove("apple")
print(emptyList)

# Remove a student name from the list. 
studentNames = ['Ali Shah', 'Khan shah', "zohaib", "Rahat ", "obaid shah"]
studentNames.remove("zohaib")
print(studentNames)


# pop() Practice
# Remove the last element using pop().
studentNames.pop(-1)
print(studentNames)

# Remove the element at index 2.
popElement = studentNames.pop(2)
print(studentNames)

# Store the popped value in a variable and print it.
print("the pop element is : " , popElement)

#Q27.  Create a list of numbers:append a new number, sort the list, reverse the list, remove one number

num = [20,30,40,94,60]
num.append(70)
num.sort()
print("Sorting Number List: ",num)
num.reverse()
num.remove(30)

print(num)


# Create a to-do list program:
# add tasks
# remove tasks
# display tasks

todoList = []
todo = input("Enter a Task ")
todoList.append(todo)
print(todoList)
todoList.remove(todo)
print(todoList)

# Take 5 numbers:sort ascending, sort descending , print reversed list
nums = [4, 1, 7, 9 ,2]
nums.sort();
nums.sort(reverse= True)
print(nums)

# Create a shopping cart list:insert item, append item, remove item, pop last item

cartList = ['clothes', 'chips','chapal' , 'Daal']
cartList.insert(0, 'shalwar qamees')
print(cartList)
cartList.append("chawal")
print(cartList)
cartList.remove('Daal')
cartList.pop(-1)
print(cartList)

#Find the largest number in a list 
numbersList = [5,30,60,20,150]
largest = max(numbersList)
print(largest)

#Find the smallest number in the list 
smallesValue = min(numbersList)
print(smallesValue)

print(type(numbersList))