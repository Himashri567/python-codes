list1=[]
list2=[]
num= int(input("Enter the length: "))
print("Enter +ve & -ve numbers: ")
for x in range(num):
    data=int(input())
    list1.append(data)
print(list1)
for x in list1:
    if(x>0):
         list2.append(x)
print(list2)