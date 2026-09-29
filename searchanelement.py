n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter number to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Number is present in the array.")
        print("Position:", i + 1)
        found = True
        break

if found == False:
    print("Number is not present in the array.")

    age = 18
    if age >= 18:
        print("You are eligible to vote.")

    else :
        print("You are not eligible to vote.")