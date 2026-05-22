# Loops in python 
# for loop

for i in range(5):
    print(i, "\n")


for i in range(1,11):
    print(i)

# Loop through a string 
name = "Hasnain Khan"

for char in name:
    print(char)
print("\n")
print("The length of the name is:", len(name))


# Loop through a list
fruits = ['apple', 'banana', 'cherry', 'orange', 'grape']

for fruit in fruits:
    print(fruit)

tasks = ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]
for task in tasks:
    print(task)

tasks = ["search", "summarize", "email"]

for task in tasks:
    print("Executing:", task)

# break statement in loop
for i in range(10):
    if i == 5:
        break
    print(i, "\n")

print("Continue statement in loop")
# continue statement in loop
for i in range(10):
    if i == 5:
        continue
    print(i, "\n")

# While loop 
count = 0

while count <= 10:
    print(count)
    count += 1

print("\nEven numbers from 1 to 20:")
# print even number from 1 to 20
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1


# print odd number from 1 to 20
print("\nOdd numbers from 1 to 20:")
num = 1
while num <= 20:
    if num % 2 != 0:
        print(num)
    num += 1

for i in range(6):
    print("Amir Shah")

string = 'Amir shah'

for i in string:
    print(i)

count = 10

while count > 0:
    print(count)
    count -= 1

tasks = ["Search", "Analyze", "Reply"]

for task in tasks:
    print("Running:", task)


for i in range(1,11):
    print('5 *', i, '=', 5 * i)


# Print star pattern using nested loops.

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()