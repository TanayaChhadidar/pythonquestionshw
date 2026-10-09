#add2 numbetrs at 3rd position of the list and append one name in the list and then split it 
a = [10, 20, 30, 40, "Sonal"]

a.insert(2, 15)
a.insert(3, 25)

a.append("Tanaya")

print("Original list:", a)

print("First part:", a[:3])
print("Second part:", a[3:])    
