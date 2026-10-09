#accept the name and check if its palindrome or not
name=input("Enter the name:")
rev=name[::-1]
if(name==rev):
    print("The name is a palindrome")
else:
    print("The name is not a palindrome")