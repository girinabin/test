# #difference between tuples and list:
# tuples are immutable,once it is created we can't update it.tuples are faster than list .eg
# tule = ('sunday','monday')
#
# list are mutable.eg
# list = ['ram','hari']


def dlist(l):
    rlist = []
    for i in range(len(l)-5):
        a=l.pop()
        rlist.append(a)
    rlist.reverse()
    return rlist
num=[1,2,3,4,5,6,7,8,9]
print(dlist(num))