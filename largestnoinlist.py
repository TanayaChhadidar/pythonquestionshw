numbers = [10, 25, 7, 45, 30]

largest = numbers[0]
second = numbers[0]

for n in numbers:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest =", second)