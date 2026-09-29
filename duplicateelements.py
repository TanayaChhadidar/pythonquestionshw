n = int(input("Enter number of elements: "))
arr = []
for i in range(n):

    num = int(input("Enter element: "))
    arr.append(num)
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)

print("Array after removing duplicates:", unique_arr)