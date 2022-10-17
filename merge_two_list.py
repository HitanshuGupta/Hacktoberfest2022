listsize1 = int(input("Enter the size no. "))

mylist1 =[]

for i in range(0, listsize1):
    num1 = int(input("Enter the number "))
    mylist1.append(num1)


listsize2 = int(input("Enter the size no. "))

mylist2 =[]

for i in range(0, listsize2):
    num2 = int(input("Enter the number "))
    mylist2.append(num2)

merge = mylist1 + mylist2

merge.sort()
print(merge)