import operator
w=input("Please enter a string: ")
a=w.lower()
def most_frequent(string):
    d={}
    for key in string:
        if key in d.keys():
            d[key]+=1
        else:
            d[key]=1  
            
    d_sort= dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    for x in d_sort:
        print(x,d_sort[x])

most_frequent(a)