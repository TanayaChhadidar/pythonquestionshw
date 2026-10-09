a = [10, "Tanaya", 25, "Rahul", 40, "Priya"]

highest = max(i for i in a if isinstance(i, int))

index = a.index(highest)

print(a[:index])
print(a[index:])