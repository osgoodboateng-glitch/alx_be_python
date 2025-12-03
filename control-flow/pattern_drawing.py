pattern = int(input("Enter the size of the pattern: "))
row = 0
while row<pattern:
    for char in range(pattern):
        print("*", end = "")
    print()