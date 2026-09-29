n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

zeros = arr.count(0)
arr = [x for x in arr if x != 0]
arr.extend([0] * zeros)

print("Array after moving zeros to the end:", arr)