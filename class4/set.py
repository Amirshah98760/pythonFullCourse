# Sets are unordered collections of unique elements. They are defined using curly braces {} or the set() constructor.

collection = { 1, 2, 3, 4, 5 }
print(collection)
print(len(collection))

for item in collection:
    print(item)

print(3 in collection, "\n")  # Check if an element is in the set

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
thisset.add("orange")
thisset.add("grapes")
print(thisset)

for x in thisset:
    print(list(thisset).index(x), x)  #We cannot access set so i wrap the set in list to access the index of element in set and print the element with index number


list = [1, 2, 3, 4, 5]   # List 

for i in list:
    print(list.index(i), i)

nums = {1, 2, 2, 3, 4, 4}  # Set are only print unique element so it will print only 1, 2, 3, 4 and its eliminate the duplicate element in set.

print(nums)

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
fruits.add("grapes")
fruits.add("apple")  # It will not add apple because apple is already in the set and set only store unique element
print(fruits)

fruits.add(('kiwi', 'melon'))  # It will add tuple in set because tuple is immutable
print(fruits)

fruits.remove("banana")
fruits.remove("grapes")
print(fruits)


fruits.update(["kiwi", "melon", "berry"])  # It will add multiple element in the set
print(fruits)

fruits.update(("mango", "papaya"))  # It will add multiple element in the set
print(fruits)
fruits.update(["peach", "pear"])  
print(fruits)

fruits.clear()  # It will remove all the element from the set
print(fruits)

a= {1,2,3}
b = {3,4,5}

print(a.union(b))

# Create a set of 5 numbers.
c = {2, 4, 6, 8, 10}
print(c)
# Add a new number using add().
c.add(12)
print(c)

fruitsName = {'apple', 'banana', 'cherry'}
# Add multiple fruits using update().
fruitsName.update(['mange', 'papaya','peach', 'pear'])
print(fruitsName)
# Remove an item using remove().
fruitsName.remove('apple')

# Find the length of a set using len().
print(len(fruitsName))

c = {2, 3, 5, 6,7}
d = {10, 12, 32, 23}

print(c.union(d))

# Count unique words in a sentence
sentence = "hello world i am learning python programming hello python"
words = sentence.split()  # Split the sentence into words
unique_words = set(words) 
print("Unique words in the sentence:", unique_words)
print("Number of unique words:", len(unique_words))

# Find duplicate numbers in a list using sets.

numbers = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 9, 1]
duplicate_numbers = set()
unique_numbers = set()

for n in numbers:
    if n in unique_numbers:
        duplicate_numbers.add(n)
    else:
        unique_numbers.add(n)

print("Duplicate numbers:", duplicate_numbers)
print("Unique numbers:", unique_numbers)
