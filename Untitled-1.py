num=int(input("Enter the num:"))
for i in range (num) :
    for j in range (1,num-i+1) :
        print(j,end="")

    for j in range (2,num-i+1) :
        print(j,end="")
    else :
        print(" ",end=" ")
    print()