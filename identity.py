matsize = int(input("Enter the size of marix: "))

for i in range(0, matsize):
    for j in range(0, matsize):
        if(i==j):
            print("1", sep=' ', end=' ')
        else:
            print("0", sep=' ', end=' ')

    print()