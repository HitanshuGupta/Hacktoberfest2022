listsize = int(input("What is the size of list:"))

mylist = []

for i in range(0, listsize):
    num = int(input("The number is: "))
    mylist.append(num)

average = sum(mylist)/listsize

print("The average of the list is ",round(average, 4))
