def main():
    n = int(input("Enter the number of elements: "))
    arr = []
    print("Enter the elements:")
    for _ in range(n):
        arr.append(int(input()))
    total_sum = sum(arr)
    print("The sum of all elements is:", total_sum)

if __name__ == "__main__":
    main()