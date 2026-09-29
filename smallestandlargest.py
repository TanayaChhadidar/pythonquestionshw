n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]
smallest = arr[0]

second_largest = None
second_smallest = None

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num != smallest and (second_smallest is None or num < second_smallest):
        second_smallest = num

print("Largest element:", largest)
print("Second largest element:", second_largest)
print("Smallest element:", smallest)
print("Second smallest element:", second_smallest)