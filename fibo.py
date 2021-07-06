limit= int(input("Enter the ending limit of the fibonacci series:"))
a=0
b=1
c=a+b
print(a,",",b,",",c,",", end="")
i=3
while i<=limit:
    a=b
    b=c
    c=a+b
    if i<limit:
        print(c,",", end="")
    else:
        print(c)
    i=i+1