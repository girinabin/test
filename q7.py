def aappend(item , lst):
    lst = []
    lst.append(item)
    return lst

a = aappend(1, [])
print(a)#output will be [1]

b = aappend(2, a)
print(b)#output will be [2] because list a will be a[1]=[] so it is initilize to empty list

c = aappend(3, [])
print(c)#output will be [3]