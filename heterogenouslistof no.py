#create a heterogenious list of nuimbers and names split the list from highest number

my_list = [10, "Tanaya", 25, "Rahul", 15, "Priya", 40, "Amit"]

numbers = [i for i in my_list if isinstance(i, int)]

highest = max(numbers)

print("Original list:", my_list)
print("Highest number:", highest)

index = my_list.index(highest)

list1 = my_list[:index]
list2 = my_list[index:]

print("First part:", list1)
print("Second part:", list2)