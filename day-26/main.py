#List Comprehension
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# new_list = [new_item for item in list]
numbers_list = [1, 2, 3]
new_list2 = [n + 1 for n in numbers_list]
print(new_list2)

name = "John"
letters_list = [letter for letter in name]
print(letters_list)

#range
range_list = [x * 2 for x in range(1, 5)]
print(range_list)

names = ["Alex", "John", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)
print(long_names)

with open("file1.txt") as file:
    file1 = file.read().splitlines()
    print(file1)

with open("file2.txt") as file:
    file2 = file.read().splitlines()
    print(file2)

# Find common items in file1 and file2 and put result in a new list using list comprehension
result = [int(num) for num in file1 if num in file2]
print(result)





